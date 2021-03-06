#!/usr/bin/env zsh
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-15 17:15:07 (UTC+0200)

func runcmd () {
    OUTPUT=$(eval $1)
    echo "\`\`\`"
    echo "$ $1\n"
    echo "$OUTPUT"
    echo "\`\`\`"
}

cat << EOF
# md_extract_frames -- mdx command line tool to extract frames from MD trajectories
Extract list of frames from a MD trajectory file using PyMol library
## Install
Clone the repository and then link \`md_extract_frames.py\` as \`mdx\` somewhere in your \`\$PATH\` (e.g. \`\$HOME/bin\`):
\`\`\`bash
ln -s \$PWD/md_extract_frames.py \$HOME/bin/mdx
\`\`\`
## Usage
EOF

runcmd "mdx -h"

echo "Extract frames from a dcd trajectory file:"
runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--frames 1 3 5 12 \
--out out.dcd"

echo "Extract frames from a dcd trajectory file with a selection of a subset of atoms:"
runcmd "mdx --select 'resi 42-60' \
--top data/2lj5.pdb \
--traj data/2lj5.dcd \
--frames 1 3 5 12 \
--out out2.dcd"

echo "If no \`--frames\` argument is given all the frames are extracted with the given selection:"
runcmd "mdx --select 'resi 42-60' \
--top data/2lj5.pdb \
--traj data/2lj5.dcd \
--out out3.dcd" | headtail -

echo "To limit memory usage for large trajectories you can split large trajectory files with the \`--lim\` option: "
runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--out out.dcd \
--lim 2000000" | headtail -
echo "The command above will generate 3 dcd files:"
runcmd "ls -lh out_????.dcd"

echo "The command can also generate numpy object files (\`npy\` files):"
runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--out out.npy \
--lim 2000000" | headtail -
echo "The command above will generate 3 \`npy\` files:"
runcmd "ls -lh out_????.npy"

runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--frames 1 3 5 12 \
--out out.npy" | headtail -
echo "The numpy array format is as below:"
runcmd 'python3 -c "import numpy; data = numpy.load(\"out.npy\"); print(data.shape)"'

echo "\`mdx\` can also align a trajectory, for example on the first frame \`--align 1\` option:"
runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--out out_aligned.dcd \
--align 1" | headtail -
echo "Along with the aligned trajectory file the command generate a file with the rmsd values:"
runcmd "cat out_aligned_rmsd.txt | head"
