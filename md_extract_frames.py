#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-15 16:42:57 (UTC+0200)

import sys
import argparse
import os
from pathlib import Path
home = str(Path.home())
sys.path.append(f'{home}/source/pymol-psico')
from pymol import cmd
import psico.fullinit
from psico.exporting import *

parser = argparse.ArgumentParser(description='Extract list of frames from a dcd file')
parser.add_argument('--top', type=str, help='Topolgy file', required=True)
parser.add_argument('--traj', type=str, help='Trajectory file', required=True)
parser.add_argument('--frames', type=int, nargs='+',
                    help='Frame ids to extract. 1-based numbering.',
                    required=False)
parser.add_argument('--out', type=str, help='output dcd file name',
                    required=True)
parser.add_argument('--select', type=str, help='Select a subset of atoms',
                    required=False)
args = parser.parse_args()

cmd.load(args.top, 'inp')
if args.frames is not None:
    stop = max(args.frames)
else:
    stop = -1
cmd.load_traj(args.traj, 'inp', state=1, stop=stop)
if args.select is None:
    selection = 'inp'
else:
    selection = f'inp and ({args.select})'
if args.frames is not None:
    frames = args.frames
else:
    frames = range(1, cmd.count_states(selection) + 1)
for f in frames:
    cmd.create('out', selection=selection, source_state=f, target_state=-1)
# Save the trajectory
cmd.save_traj(args.out, 'out')
# Save the topology
topfilename = f'{os.path.splitext(args.out)[0]}.pdb'
cmd.save(topfilename, selection=selection, state=1)
