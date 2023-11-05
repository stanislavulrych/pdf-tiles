# pdf-tiles

pdf-tiles is a free and open-source utility for arranging multiple pdfs with stickers into a single page.

## Usage

```
    python pdf-tiles.py <horizontal items count> <vertical items count> <file 1> .. <file N>
```

Will take top-left corner of first page of each `file X` and produce a layout of (`xcount` x `ycount`) tiles.

Use `-` to omit the file.

Currently only limited to A4 format.

Output file is always `out.pdf`.


## Example

Merge the top left (A6) corners of 1.pdf 2.pdf 3.pdf 4.pdf into a single page

    1 |           2 |          3 |          4 |                  1 | 2
    --|--         --|--        --|--        --|--      ===>      --|--
      |             |            |            |                  3 | 4

by
    python pdf-tiles.py 2 2 1.pdf 2.pdf 3.pdf 4.pdf
    


## Contributions

Maintaining `pdf-tiles` is a collaborative effort. You can support the project by
writing documentation and submitting code.

