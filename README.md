# sewing_tools
A collection of sewing adjacent tools.

## Quick guide for make_tiles.py

This is a tool that can take poster sized pdf files, and tile them into 8.5 x 11 pages for printing at home.

Set up your environment:
`conda create -n make-tiles-env pypdf2`

Run script:
`python tiler.py -i in.pdf -o tiled_out.pdf -w <> -l <>`
