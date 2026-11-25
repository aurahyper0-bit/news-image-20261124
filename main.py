#!/usr/bin/env python3
"""Sum up 24 November 2026's world news in one image.

The front page (entry.png, drawn in this session as a newspaper:
four tankers hit by mines in the Strait of Hormuz as the lead, plus
Huawei's US conviction, Ukraine's strikes on Russian ships, the
Hamas security chief killed in Gaza, Huang back at Nvidia, a Turkish
helicopter crash and the Cartagena hostages) is copied to
/output/entry.png.

Standard library only, no network; running it twice writes the
same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
