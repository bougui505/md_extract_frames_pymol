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
 ObjectMolecule: read set 295 into state 295...
 ObjectMolecule: read set 296 into state 296...
 ObjectMolecule: read set 297 into state 297...
 ObjectMolecule: read set 298 into state 298...
 ObjectMolecule: read set 299 into state 299...
 ObjectMolecule: read set 300 into state 300...
 ObjectMolecule: read set 301 into state 301...
 PyMOL not running, entering library mode (experimental)
Getting state 1/301Getting state 2/301Getting state 3/301Getting state 4/301Getting state 5/301Getting state 6/301Getting state 7/301Getting state 8/301Getting state 9/301Getting state 10/301Getting state 11/301Getting state 12/301Getting state 13/301Getting state 14/301Getting state 15/301Getting state 16/301Getting state 17/301Getting state 18/301Getting state 19/301Getting state 20/301Getting state 21/301Getting state 22/301Getting state 23/301Getting state 24/301Getting state 25/301Getting state 26/301Getting state 27/301Getting state 28/301Getting state 29/301Getting state 30/301Getting state 31/301Getting state 32/301Getting state 33/301Getting state 34/301Getting state 35/301Getting state 36/301Getting state 37/301Getting state 38/301Getting state 39/301Getting state 40/301Getting state 41/301Getting state 42/301Getting state 43/301Getting state 44/301Getting state 45/301Getting state 46/301Getting state 47/301Getting state 48/301Getting state 49/301Getting state 50/301Getting state 51/301Getting state 52/301Getting state 53/301Getting state 54/301Getting state 55/301Getting state 56/301Getting state 57/301Getting state 58/301Getting state 59/301Getting state 60/301Getting state 61/301Getting state 62/301Getting state 63/301Getting state 64/301Getting state 65/301Getting state 66/301Getting state 67/301Getting state 68/301Getting state 69/301Getting state 70/301Getting state 71/301Getting state 72/301Getting state 73/301Getting state 74/301Getting state 75/301Getting state 76/301Getting state 77/301Getting state 78/301Getting state 79/301Getting state 80/301Getting state 81/301Getting state 82/301Getting state 83/301Getting state 84/301Getting state 85/301Getting state 86/301Getting state 87/301Getting state 88/301Getting state 89/301Getting state 90/301Getting state 91/301Getting state 92/301Getting state 93/301Getting state 94/301Getting state 95/301Getting state 96/301Getting state 97/301Getting state 98/301Getting state 99/301Getting state 100/301Getting state 101/301Getting state 102/301Getting state 103/301Getting state 104/301Getting state 105/301Getting state 106/301Getting state 107/301Getting state 108/301Getting state 109/301Getting state 110/301Getting state 111/301Getting state 112/301Getting state 113/301Getting state 114/301Getting state 115/301Getting state 116/301Getting state 117/301Getting state 118/301Getting state 119/301Getting state 120/301Getting state 121/301Getting state 122/301Getting state 123/301Getting state 124/301Getting state 125/301Getting state 126/301Getting state 127/301Getting state 128/301Getting state 129/301Getting state 130/301Getting state 131/301Getting state 132/301Getting state 133/301Getting state 134/301Getting state 135/301Getting state 136/301Getting state 137/301Getting state 138/301Getting state 139/301Getting state 140/301Getting state 141/301Getting state 142/301Getting state 143/301Getting state 144/301Getting state 145/301Getting state 146/301Getting state 147/301Getting state 148/301Getting state 149/301Getting state 150/301Getting state 151/301Getting state 152/301Getting state 153/301Getting state 154/301Getting state 155/301Getting state 156/301Getting state 157/301Getting state 158/301Getting state 159/301Getting state 160/301Getting state 161/301Getting state 162/301Getting state 163/301Getting state 164/301Getting state 165/301Getting state 166/301Getting state 167/301Getting state 168/301Getting state 169/301Getting state 170/301Getting state 171/301Getting state 172/301Getting state 173/301Getting state 174/301Getting state 175/301Getting state 176/301Getting state 177/301Getting state 178/301Getting state 179/301Getting state 180/301Getting state 181/301Getting state 182/301Getting state 183/301Getting state 184/301Getting state 185/301Getting state 186/301Getting state 187/301Getting state 188/301Getting state 189/301Getting state 190/301Getting state 191/301Getting state 192/301Getting state 193/301Getting state 194/301Getting state 195/301Getting state 196/301Getting state 197/301Getting state 198/301Getting state 199/301Getting state 200/301Getting state 201/301Getting state 202/301Getting state 203/301Getting state 204/301Getting state 205/301Getting state 206/301Getting state 207/301Getting state 208/301Getting state 209/301Getting state 210/301Getting state 211/301Getting state 212/301Getting state 213/301Getting state 214/301Getting state 215/301Getting state 216/301Getting state 217/301Getting state 218/301Getting state 219/301Getting state 220/301Getting state 221/301Getting state 222/301Getting state 223/301Getting state 224/301Getting state 225/301Getting state 226/301Getting state 227/301Getting state 228/301Getting state 229/301Getting state 230/301Getting state 231/301Getting state 232/301Getting state 233/301Getting state 234/301Getting state 235/301Getting state 236/301Getting state 237/301Getting state 238/301Getting state 239/301Getting state 240/301Getting state 241/301Getting state 242/301Getting state 243/301Getting state 244/301Getting state 245/301Getting state 246/301Getting state 247/301Getting state 248/301Getting state 249/301Getting state 250/301Getting state 251/301Getting state 252/301Getting state 253/301Getting state 254/301Getting state 255/301Getting state 256/301Getting state 257/301Getting state 258/301Getting state 259/301Getting state 260/301Getting state 261/301Getting state 262/301Getting state 263/301Getting state 264/301Getting state 265/301Getting state 266/301Getting state 267/301Getting state 268/301Getting state 269/301Getting state 270/301Getting state 271/301Getting state 272/301Getting state 273/301Getting state 274/301Getting state 275/301Getting state 276/301Getting state 277/301Getting state 278/301Getting state 279/301Getting state 280/301Getting state 281/301Getting state 282/301Getting state 283/301Getting state 284/301Getting state 285/301Getting state 286/301Getting state 287/301Getting state 288/301Getting state 289/301Getting state 290/301Getting state 291/301Getting state 292/301Getting state 293/301Getting state 294/301Getting state 295/301Getting state 296/301Getting state 297/301Getting state 298/301Getting state 299/301Getting state 300/301Getting state 301/301
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
 ObjectMolecule: read set 295 into state 94...
 ObjectMolecule: read set 296 into state 95...
 ObjectMolecule: read set 297 into state 96...
 ObjectMolecule: read set 298 into state 97...
 ObjectMolecule: read set 299 into state 98...
 ObjectMolecule: read set 300 into state 99...
 ObjectMolecule: read set 301 into state 100...

Getting state 1/100Getting state 2/100Getting state 3/100Getting state 4/100Getting state 5/100Getting state 6/100Getting state 7/100Getting state 8/100Getting state 9/100Getting state 10/100Getting state 11/100Getting state 12/100Getting state 13/100Getting state 14/100Getting state 15/100Getting state 16/100Getting state 17/100Getting state 18/100Getting state 19/100Getting state 20/100Getting state 21/100Getting state 22/100Getting state 23/100Getting state 24/100Getting state 25/100Getting state 26/100Getting state 27/100Getting state 28/100Getting state 29/100Getting state 30/100Getting state 31/100Getting state 32/100Getting state 33/100Getting state 34/100Getting state 35/100Getting state 36/100Getting state 37/100Getting state 38/100Getting state 39/100Getting state 40/100Getting state 41/100Getting state 42/100Getting state 43/100Getting state 44/100Getting state 45/100Getting state 46/100Getting state 47/100Getting state 48/100Getting state 49/100Getting state 50/100Getting state 51/100Getting state 52/100Getting state 53/100Getting state 54/100Getting state 55/100Getting state 56/100Getting state 57/100Getting state 58/100Getting state 59/100Getting state 60/100Getting state 61/100Getting state 62/100Getting state 63/100Getting state 64/100Getting state 65/100Getting state 66/100Getting state 67/100Getting state 68/100Getting state 69/100Getting state 70/100Getting state 71/100Getting state 72/100Getting state 73/100Getting state 74/100Getting state 75/100Getting state 76/100Getting state 77/100Getting state 78/100Getting state 79/100Getting state 80/100Getting state 81/100Getting state 82/100Getting state 83/100Getting state 84/100Getting state 85/100Getting state 86/100Getting state 87/100Getting state 88/100Getting state 89/100Getting state 90/100Getting state 91/100Getting state 92/100Getting state 93/100Getting state 94/100Getting state 95/100Getting state 96/100Getting state 97/100Getting state 98/100Getting state 99/100Getting state 100/100
```
The command above will generate 3 dcd files:
```
$ ls -lh out_????.dcd

-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:33 out_0000.dcd
-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:33 out_0001.dcd
-rw-r--r--. 1 bougui bis 1.5M Jun 18 11:33 out_0002.dcd
```
