# Optional local pixel cleanup

Use after generation when the user requests aligned pixel grids or a native-resolution sprite for editing. This adapter calls [Perfect Pixel by theamusing](https://github.com/theamusing/perfectPixel); upstream code is not bundled, copied, or installed automatically.

## Setup

Use a dedicated virtual environment. The commands below are an explicit optional setup, not part of loading the skill. Package installation downloads third-party code from PyPI; it does not require a GitHub account, SSH key, or image-generation API key. Respect the user's existing authorization for installation.

Run from the skill directory:

```bash
python3 -m venv .venv-pixel
.venv-pixel/bin/python -m pip install 'perfect-pixel[opencv]==0.1.4' Pillow
```

On Windows, the interpreter is `.venv-pixel\Scripts\python.exe`. The Perfect Pixel version is pinned to the reviewed API; transitive dependencies are not fully locked. Do not distribute the environment with the skill.

## Process a single asset

```bash
.venv-pixel/bin/python scripts/refine_pixels.py input.png output/sprite-native.png

# Optional: manually suggest grid counts if automatic detection is wrong.
.venv-pixel/bin/python scripts/refine_pixels.py input.png output/sprite-manual.png --grid 64 64
```

The wrapper processes local image pixels, makes no network requests, and requires a new PNG destination. Keep the original. Open the native output in Aseprite and zoom in for preview; do not edit a large rescaled promotional image as though each screen pixel were one sprite pixel.

## Limits that matter

- Grid counts are estimates; even a manual grid can produce slightly different output dimensions after refinement. Report actual dimensions. Do not promise exact 64 x 64 delivery without a separate requested canvas adjustment.
- Inspect facial features, thin outlines and small accessories. Resampling may remove them; this is not a semantic repair model and does not create missing details or animation frames.
- Work on a single extracted asset when a sheet or collage uses different pixel scales. Do not run the global grid estimator over an entire promotional poster with text.
- This wrapper rejects transparent inputs and animations. The documented upstream API is RGB; silently discarding alpha would damage cutouts. Keep transparent assets in Aseprite until an alpha-aware path is implemented and checked.
- The algorithm samples colors per grid cell. It does not enforce a chosen global palette size; palette editing remains a separate Aseprite step.

## Attribution and licensing

The upstream [pyproject.toml](https://github.com/theamusing/perfectPixel/blob/main/pyproject.toml) declares MIT. At review time, its repository root did not show a standalone complete LICENSE file. This package provides an independently written caller and installation instructions only. Before redistributing upstream source or binaries, obtain the applicable complete copyright and license notices and include them. Do not replace the upstream author with the skill author's name. Acknowledgement alone does not replace required license notices.

The MIT license for this skill covers its own code and instructions. Third-party software and image references retain their own terms. The cleanup step does not confer rights in source artwork.
