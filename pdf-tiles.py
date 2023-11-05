import sys
from pypdf import PdfReader, PdfWriter, Transformation, PaperSize

ainit = 3

if len(sys.argv) <= ainit:
    print(f"Usage:\n")
    print(f"    python pdf-tiles.py <horizontal items> <vertical items> <file 1> .. <file N>")
    print(f"\nWill take top-left corner of first page of each <file X> and produce a layout of (xcount x ycount) tiles.")
    print(f"Use '-' to omit the file.\n")
    print(f"Currently only limited to A4 format.\n")
    print(f"Output file is always `out.pdf`.\n")
    
    print(f"\nExample: Merge the top left (A6) corners of 1.pdf 2.pdf 3.pdf 4.pdf into a single page\n")
    print(f"    1 |           2 |          3 |          4 |                  1 | 2")
    print(f"    --|--         --|--        --|--        --|--      ===>      --|--")
    print(f"      |             |            |            |                  3 | 4")
    print(f"\nby\n")
    print(f"    python pdf-tiles.py 2 2 1.pdf 2.pdf 3.pdf 4.pdf")
    print(f"\n")
    exit(1)

xsize = PaperSize.A4.width
ysize = PaperSize.A4.height

xcount = int(sys.argv[1])
ycount = int(sys.argv[2])

writer = PdfWriter()
destPage = writer.add_blank_page(width=xsize, height=ysize)

for i in range(len(sys.argv)-ainit):
    f = sys.argv[i+ainit]
    if f == "-":
        continue

    reader = PdfReader(f)
    page3 = reader.pages[0]
    t = {
        "tx": (i % xcount)*(xsize/xcount),
        "ty": -(i // xcount)*(ysize/ycount) 
    }
    print(t)
    page3.add_transformation(Transformation().translate(**t))
    destPage.merge_page(page3)

with open("out.pdf", "wb") as fp:
    writer.write(fp)
