#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-15 16:42:57 (UTC+0200)

import pymol.cmd as cmd
import argparse

parser = argparse.ArgumentParser(description='Extract list of frames from a dcd file')
parser.add_argument('--top', type=str, help='Topolgy file')
parser.add_argument('--traj', type=str, help='Trajectory file')
parser.add_argument('--frames', type=int, nargs='+',
                    help='Frame ids to extract. 1-based numbering.')
parser.add_argument('--out', '-o', type=str, help='output dcd file name')
args = parser.parse_args()

cmd.load(args.top)
cmd.load_traj(args.pdb, state=1)
cmd.create('out', source_state=args.frames)
cmd.save_traj(args.out, 'out')
