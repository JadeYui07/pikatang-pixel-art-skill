#!/usr/bin/env python3
"""Optional local Perfect Pixel adapter. No downloads or network calls."""

import argparse
from pathlib import Path


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path, help="new native-resolution PNG")
    parser.add_argument("--grid", type=positive_int, nargs=2, metavar=("WIDTH", "HEIGHT"),
                        help="override estimated grid counts; actual result can differ")
    parser.add_argument("--sample", choices=("center", "median", "majority"), default="center")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error("input file does not exist")
    if args.output.suffix.lower() != ".png":
        parser.error("output must be a .png file")
    if args.output.exists():
        parser.error("output already exists; choose a new filename")
    try:
        import numpy as np
        from PIL import Image
        from perfect_pixel import get_perfect_pixel
    except ImportError:
        parser.error("optional dependencies missing; see references/pixel-cleanup.md")

    with Image.open(args.input) as source:
        if getattr(source, "n_frames", 1) != 1:
            parser.error("use a single still image, not an animation")
        rgba = source.convert("RGBA")
        if rgba.getchannel("A").getextrema()[0] < 255:
            parser.error("transparent inputs are not supported; preserve alpha in Aseprite instead")
        rgb = np.asarray(rgba.convert("RGB"))

    width, height, pixels = get_perfect_pixel(
        rgb, sample_method=args.sample,
        grid_size=tuple(args.grid) if args.grid else None,
        fix_square=False, debug=False,
    )
    if width is None or height is None:
        parser.error("grid detection failed; original preserved. Try --grid WIDTH HEIGHT")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("xb") as output:
        Image.fromarray(np.asarray(pixels, dtype=np.uint8)).save(output, format="PNG")
    print(f"Saved native grid: {width} x {height} pixels -> {args.output}")


if __name__ == "__main__":
    main()
