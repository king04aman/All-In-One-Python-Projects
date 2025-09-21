from PyPDF2 import PdfFileMerger
import argparse
import sys

try:
    from PyPDF2 import PdfMerger  # new name
except ImportError:
    from PyPDF2 import PdfFileMerger as PdfMerger  # fallback for older versions


def by_appending():
    merger = PdfFileMerger()
    f1 = open("testPDF1.pdf", "rb")
    merger.append(f1)
    merger.append("testPDF12.pdf")

    merger.write("mergedPDF.pdf")
    f1.close

def by_inserting():
    merger = PdfFileMerger()
    merger.append("testPDF1.pdf")
    merger.merge(0, "testPDF2.pdf")
    merger.write("mergedPDF.pdf")

    def merge_pdfs(pdfs: list[Path], output: Path) -> None:
    """Append all given PDFs in order and write to output."""
    merger = PdfMerger()
    files = []
    try:
        for pdf in pdfs:
            fh = pdf.open("rb")
            files.append(fh)
            merger.append(fh)
        merger.write(str(output))
        print(f"[ok] Merged {len(pdfs)} PDFs into {output}")
    finally:
        for fh in files:
            fh.close()


def insert_pdf(pdfs: list[Path], insert: Path, index: int, output: Path) -> None:
    """Append PDFs and insert another at given index."""
    merger = PdfMerger()
    files = []
    try:
        for pdf in pdfs:
            fh = pdf.open("rb")
            files.append(fh)
            merger.append(fh)

        with insert.open("rb") as ins_fh:
            merger.merge(index, ins_fh)

        merger.write(str(output))
        print(f"[ok] Inserted {insert} at index {index} -> {output}")
    finally:
        for fh in files:
            fh.close()


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Merge multiple PDFs")
    parser.add_argument("pdfs", nargs="+", help="Input PDF files")
    parser.add_argument("-o", "--output", default="mergedPDF.pdf", help="Output file name")
    parser.add_argument("--insert", help="Optional PDF to insert")
    parser.add_argument("--at", type=int, default=0, help="Index to insert at (default=0)")
    return parser.parse_args(argv)


def validate(paths: list[str]) -> list[Path]:
    pdfs = []
    for p in paths:
        path = Path(p)
        if not path.exists():
            sys.exit(f"[error] File not found: {path}")
        if path.suffix.lower() != ".pdf":
            sys.exit(f"[error] Not a PDF: {path}")
        pdfs.append(path)
    return pdfs


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    pdfs = validate(args.pdfs)
    out = Path(args.output)

    if args.insert:
        insert = validate([args.insert])[0]
        insert_pdf(pdfs, insert, args.at, out)
    else:
        if len(pdfs) < 2:
            sys.exit("[error] Need at least 2 PDFs to merge")
        merge_pdfs(pdfs, out)



if __name__ == "__main__":

    by_appending()
    by_inserting()

    main()
