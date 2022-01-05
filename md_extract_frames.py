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
from pymol import cmd
import psico.fullinit
from psico.exporting import *

parser = argparse.ArgumentParser(
    description='Extract list of frames from a dcd file')
parser.add_argument('--top', type=str, help='Topolgy file', required=True)
parser.add_argument('--traj', type=str, help='Trajectory file', required=True)
parser.add_argument('--frames',
                    type=int,
                    nargs='+',
                    help='Frame ids to extract. 1-based numbering.',
                    required=False)
parser.add_argument(
    '--fframes',
    type=str,
    help='Frame ids to extract. 1-based numbering given as a file.',
    required=False)
parser.add_argument('--out',
                    type=str,
                    help='output dcd or npy file name',
                    required=True)
parser.add_argument('--select',
                    type=str,
                    help='Select a subset of atoms',
                    required=False)
parser.add_argument('--align',
                    type=int,
                    help='Align on the given frame (starting from 1)',
                    default=None)
parser.add_argument(
    '--limit',
    type=int,
    help=
    'Limit the size of the trajectory file to this limit in bytes. If the limit is reached the trajectory file is loaded by chunk accordingly. The default is no threshold'
)
args = parser.parse_args()

# For memory efficiency:
cmd.set('defer_builds_mode', 3)
# To keep original atom order
cmd.set('retain_order', 1)

if args.fframes is not None:
    args.frames = list(numpy.genfromtxt(args.fframes, dtype=int))

cmd.load(args.top, 'inp')

# Check the size of the input trajectory file
trajfilesize = os.path.getsize(args.traj)
tfthreshold = args.limit
if tfthreshold is None:
    nchunks = 1
else:
    nchunks = int(numpy.ceil(trajfilesize / tfthreshold))
nframes = dcd_reader.get_nframes(args.traj)
chunks = numpy.array_split(numpy.arange(1, nframes + 1), nchunks)

if args.select is None:
    selection = 'inp'
else:
    selection = f'inp and ({args.select})'

if args.frames is not None:
    stop = max(args.frames)
    chunks = [c[c <= stop] for c in chunks if min(c) <= stop]
else:
    stop = -1
    args.frames = range(1, nframes + 1)
for chunkid, chunk in enumerate(chunks):
    start, stop = min(chunk), max(chunk)
    cmd.reinitialize()
    cmd.load(args.top, 'inp')
    cmd.load_traj(args.traj,
                  'inp',
                  state=1,
                  start=start,
                  stop=stop,
                  selection=selection)
    if args.align is not None:
        if len(chunks) == 1:
            rmsds = cmd.intra_fit(selection, args.align)
            rmsds[rmsds == -1.] = 0.
            outrmsdfile = f"{os.path.splitext(args.out)[0]}_rmsd.txt"
            numpy.savetxt(outrmsdfile, rmsds, fmt="%.4f")
    states = numpy.where(numpy.isin(chunk, args.frames))[0] + 1
    nstates = cmd.count_states('inp')
    if len(states) == nstates:
        cmd.create('out', selection=selection, source_state=0, target_state=-1)
    else:
        for s in states:
            sys.stdout.write(f'Getting state {s}/{max(states)}\r')
            sys.stdout.flush()
            cmd.create('out',
                       selection=selection,
                       source_state=s,
                       target_state=-1)
        sys.stdout.write('\n')
    # Save the trajectory
    extension = os.path.splitext(args.out)[1]
    if len(chunks) > 1:
        trajfilename = f'{os.path.splitext(args.out)[0]}_{chunkid:04d}{extension}'
        if extension == '.dcd':
            cmd.save_traj(trajfilename, 'out')
        else:
            coords_out = cmd.get_coords('out', state=0)
            nstates = cmd.count_states('out')
            coords_out = coords_out.reshape((nstates, -1))
            numpy.save(trajfilename, coords_out)
    else:
        if extension == '.dcd':
            cmd.save_traj(args.out, 'out')
        else:
            coords_out = cmd.get_coords('out', state=0)
            nstates = cmd.count_states('out')
            coords_out = coords_out.reshape((nstates, -1))
            numpy.save(args.out, coords_out)
# Save the topology
topfilename = f'{os.path.splitext(args.out)[0]}.pdb'
cmd.save(topfilename, selection=selection, state=1)
