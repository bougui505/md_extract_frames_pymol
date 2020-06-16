# md_extract_frames -- mdx command line tool to extract frames from MD trajectories
Extract list of frames from a MD trajectory file using PyMol library
## Install
Clone the repository and then link `md_extract_frames.py` as `mdx` somewhere in your `$PATH` (e.g. `$HOME/bin`):
```bash
ln -s md_extract_frames.py $HOME/bin/mdx
```
## Usage
```
$ mdx -h

usage: mdx [-h] --top TOP --traj TRAJ --frames FRAMES [FRAMES ...] --out OUT

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
$ mdx --top data/2lj5.pdb --traj data/2lj5.dcd --frames 1 3 5 12 --out out.dcd

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
```
