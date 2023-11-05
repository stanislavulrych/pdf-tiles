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

## Contributions

Maintaining `pdf-tiles` is a collaborative effort. You can support the project by
writing documentation and submitting code.

