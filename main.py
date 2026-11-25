#!/usr/bin/env python3
"""24 November 2026 world news, summed up in a single image.

The entry is a newspaper front page (entry.png). Its lead story is
four tankers hit by mines in the Strait of Hormuz, with Iran's
Revolutionary Guard saying its navy struck a container ship there.
Six more stories from the day fill the grid underneath: Huawei's US
conviction, Ukraine's strikes on Russian ships, the Hamas security
chief killed in Gaza, Huang back as Nvidia chief, a Turkish
helicopter crash, and 25 hostages in Cartagena.

This program's whole job is to hand that finished page to the
harness. It copies entry.png into the output directory — taken from
MAKEFUN_OUTPUT_DIR, or /output when that is unset — and checks the
copy really is a PNG before it reports success. It uses only the
Python standard library, touches no network, and writes the same
bytes on every run.
"""

import os
import shutil
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def source_path():
    return Path(__file__).resolve().parent / "entry.png"


def target_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(out)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.png"


def main():
    src = source_path()
    if not src.is_file():
        raise SystemExit("entry.png is missing next to main.py")
    dst = target_path()
    shutil.copyfile(src, dst)
    head = dst.read_bytes()[:8]
    if head != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    size = dst.stat().st_size
    if size == 0:
        raise SystemExit("entry.png is empty")
    print("wrote %s (%d bytes)" % (dst, size))


if __name__ == "__main__":
    main()
