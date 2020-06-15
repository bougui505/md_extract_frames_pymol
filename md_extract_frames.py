#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-15 16:42:57 (UTC+0200)

import sys
import argparse
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
                    required=True)
parser.add_argument('--out', type=str, help='output dcd file name',
                    required=True)
args = parser.parse_args()

cmd.load(args.top, 'inp')
cmd.load_traj(args.traj, 'inp', state=1, stop=max(args.frames))
for f in args.frames:
    cmd.create('out', selection='inp', source_state=f, target_state=-1)
cmd.save_traj(args.out, 'out')
