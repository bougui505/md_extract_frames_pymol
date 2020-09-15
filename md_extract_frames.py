#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-15 16:42:57 (UTC+0200)

import sys
import argparse
import os
import numpy
import dcd_reader
from pathlib import Path
home = str(Path.home())
sys.path.append(f'{home}/source/pymol-psico')
from pymol import cmd
import psico.fullinit
from psico.exporting import *
import numpy

parser = argparse.ArgumentParser(description='Extract list of frames from a dcd file')
parser.add_argument('--top', type=str, help='Topolgy file', required=True)
parser.add_argument('--traj', type=str, help='Trajectory file', required=True)
parser.add_argument('--frames', type=int, nargs='+',
                    help='Frame ids to extract. 1-based numbering.',
                    required=False)
parser.add_argument('--fframes', type=str,
                    help='Frame ids to extract. 1-based numbering given as a file.',
                    required=False)
parser.add_argument('--out', type=str, help='output dcd file name',
                    required=True)
parser.add_argument('--select', type=str, help='Select a subset of atoms',
                    required=False)
tfthreshold = 4000000000
parser.add_argument('--limit', type=int,
                    help=f'Limit the size of the trajectory file to this limit in bytes. If the limit is reached the trajectory file is loaded by chunk accordingly. The default is {tfthreshold} B ({tfthreshold/1000000000} GB)', default=tfthreshold)
args = parser.parse_args()

# For memory efficiency:
cmd.set('defer_builds_mode', 3)

if args.fframes is not None:
    args.frames = list(numpy.genfromtxt(args.fframes, dtype=int))

cmd.load(args.top, 'inp')

# Check the size of the input trajectory file
trajfilesize = os.path.getsize(args.traj)
tfthreshold = args.limit
nchunks = int(numpy.ceil(trajfilesize / tfthreshold))
nframes = dcd_reader.get_nframes(args.traj)
chunks = numpy.array_split(numpy.arange(1, nframes + 1), nchunks)

if args.select is None:
    selection = 'inp'
else:
    selection = f'inp and ({args.select})'

if args.frames is not None:
    stop = max(args.frames)
    chunks = [c[c<=stop] for c in chunks if min(c)<= stop]
else:
    stop = -1
    args.frames = range(1, nframes+1)
for chunkid, chunk in enumerate(chunks):
    start, stop = min(chunk), max(chunk)
    cmd.reinitialize()
    cmd.load(args.top, 'inp')
    cmd.load_traj(args.traj, 'inp', state=1, start=start, stop=stop,
                  selection=selection)
    states = numpy.where(numpy.isin(chunk, args.frames))[0] + 1
    nstates = cmd.count_states('inp')
    if len(states) == nstates:
        cmd.create('out', selection=selection, source_state=0, target_state=-1)
    else:
        for s in states:
            sys.stdout.write(f'Getting state {s}/{max(states)}\r')
            sys.stdout.flush()
            cmd.create('out', selection=selection, source_state=s, target_state=-1)
        sys.stdout.write('\n')
    # Save the trajectory
    if len(chunks) > 1:
        trajfilename = f'{os.path.splitext(args.out)[0]}_{chunkid:04d}.dcd'
        cmd.save_traj(trajfilename, 'out')
    else:
        cmd.save_traj(args.out, 'out')
# Save the topology
topfilename = f'{os.path.splitext(args.out)[0]}.pdb'
cmd.save(topfilename, selection=selection, state=1)
