```
$ ./md_extract_frames.py -h

usage: md_extract_frames.py [-h] --top TOP --traj TRAJ --frames FRAMES
                            [FRAMES ...] --out OUT

Extract list of frames from a dcd file

optional arguments:
  -h, --help            show this help message and exit
  --top TOP             Topolgy file
  --traj TRAJ           Trajectory file
  --frames FRAMES [FRAMES ...]
                        Frame ids to extract. 1-based numbering.
  --out OUT             output dcd file name
```
```
$ ./md_extract_frames.py --top data/2lj5.pdb                                --traj data/2lj5.dcd                                --frames 1 3 5 12                                --out out.dcd

dcdplugin) detected standard 32-bit DCD file of native endianness
dcdplugin) CHARMM format DCD file (also NAMD 2.1 and later)
 ObjectMolecule: read set 1 into state 1...
 ObjectMolecule: read set 2 into state 2...
 ObjectMolecule: read set 3 into state 3...
 ObjectMolecule: read set 4 into state 4...
 ObjectMolecule: read set 5 into state 5...
 ObjectMolecule: read set 6 into state 6...
 ObjectMolecule: read set 7 into state 7...
 ObjectMolecule: read set 8 into state 8...
 ObjectMolecule: read set 9 into state 9...
 ObjectMolecule: read set 10 into state 10...
 ObjectMolecule: read set 11 into state 11...
 ObjectMolecule: read set 12 into state 12...
 PyMOL not running, entering library mode (experimental)
[1, 3, 5, 12]
```
