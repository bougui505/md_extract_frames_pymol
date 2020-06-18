# md_extract_frames -- mdx command line tool to extract frames from MD trajectories
Extract list of frames from a MD trajectory file using PyMol library
## Install
Clone the repository and then link `md_extract_frames.py` as `mdx` somewhere in your `$PATH` (e.g. `$HOME/bin`):
```bash
ln -s $PWD/md_extract_frames.py $HOME/bin/mdx
```
## Usage
```
$ mdx -h

usage: mdx [-h] --top TOP --traj TRAJ [--frames FRAMES [FRAMES ...]] --out OUT
           [--select SELECT] [--limit LIMIT]

Extract list of frames from a dcd file

optional arguments:
  -h, --help            show this help message and exit
  --top TOP             Topolgy file
  --traj TRAJ           Trajectory file
  --frames FRAMES [FRAMES ...]
                        Frame ids to extract. 1-based numbering.
  --out OUT             output dcd file name
  --select SELECT       Select a subset of atoms
  --limit LIMIT         Limit the size of the trajectory file to this limit in
                        bytes. If the limit is reached the trajectory file is
                        loaded by chunk accordingly. The default is 4000000000
                        B (4.0 GB)
```
Extract frames from a dcd trajectory file:
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
Getting state 1/12Getting state 3/12Getting state 5/12Getting state 12/12
```
Extract frames from a dcd trajectory file with a selection of a subset of atoms:
```
$ mdx --select 'resi 42-60' --top data/2lj5.pdb --traj data/2lj5.dcd --frames 1 3 5 12 --out out2.dcd

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
Getting state 1/12Getting state 3/12Getting state 5/12Getting state 12/12
```
If no `--frames` argument is given all the frames are extracted with the given selection:
```
$ mdx --select 'resi 42-60' --top data/2lj5.pdb --traj data/2lj5.dcd --out out3.dcd

dcdplugin) detected standard 32-bit DCD file of native endianness
dcdplugin) CHARMM format DCD file (also NAMD 2.1 and later)
 ObjectMolecule: read set 1 into state 1...
 ObjectMolecule: read set 2 into state 2...
 ObjectMolecule: read set 3 into state 3...
 ObjectMolecule: read set 4 into state 4...
 ObjectMolecule: read set 5 into state 5...
[...]
 ObjectMolecule: read set 294 into state 294...
 ObjectMolecule: read set 295 into state 295...
 ObjectMolecule: read set 296 into state 296...
 ObjectMolecule: read set 297 into state 297...
 ObjectMolecule: read set 298 into state 298...
 ObjectMolecule: read set 299 into state 299...
 ObjectMolecule: read set 300 into state 300...
 ObjectMolecule: read set 301 into state 301...
 PyMOL not running, entering library mode (experimental)
```
To limit memory usage for large trajectories you can split large trajectory files with the `--lim` option: 
```
$ mdx --top data/2lj5.pdb --traj data/2lj5.dcd --out out.dcd --lim 2000000

dcdplugin) detected standard 32-bit DCD file of native endianness
dcdplugin) CHARMM format DCD file (also NAMD 2.1 and later)
 ObjectMolecule: read set 1 into state 1...
 ObjectMolecule: read set 2 into state 2...
 ObjectMolecule: read set 3 into state 3...
 ObjectMolecule: read set 4 into state 4...
 ObjectMolecule: read set 5 into state 5...
[...]
 ObjectMolecule: read set 294 into state 93...
 ObjectMolecule: read set 295 into state 94...
 ObjectMolecule: read set 296 into state 95...
 ObjectMolecule: read set 297 into state 96...
 ObjectMolecule: read set 298 into state 97...
 ObjectMolecule: read set 299 into state 98...
 ObjectMolecule: read set 300 into state 99...
 ObjectMolecule: read set 301 into state 100...
 PyMOL not running, entering library mode (experimental)
```
The command above will generate 3 dcd files:
```
$ ls -lh out_????.dcd

-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:59 out_0000.dcd
-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:59 out_0001.dcd
-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:59 out_0002.dcd
```
