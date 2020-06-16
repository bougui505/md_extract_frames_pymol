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
# md_extract_frames
Extract list of frames from a MD trajectory file using PyMol library
## Install
Clone the repository and then link \`md_extract_frames.py\` as \`mdx\` somewhere in your \`\$PATH\` (e.g. \`\$HOME/bin\`):
\`\`\`bash
ln -s md_extract_frames.py \$HOME/bin/mdx
\`\`\`
## Usage
EOF

runcmd "mdx -h"
runcmd "mdx --top data/2lj5.pdb \
--traj data/2lj5.dcd \
--frames 1 3 5 12 \
--out out.dcd"
