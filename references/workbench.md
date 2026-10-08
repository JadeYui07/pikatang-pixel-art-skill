# Pixel Asset Workbench

Use this guide to route a request and choose a useful deliverable. Keep the user's subject and visual references as the source of truth; the modes below are defaults, not rigid templates.

## Modes

| Mode | Useful output | Default framing |
|---|---|---|
| Character | Full-body avatar, turnaround, or pose sheet | Portrait; isolate one character on a plain background |
| Pet | Pet sprite, expression set, or view sheet | Portrait or square; keep markings and proportions consistent |
| House | Exterior illustration or architectural cutaway | 4:3; preserve the requested camera and key architectural features |
| Interior | Isometric room, top-down plan, or open cutaway | 4:3; retain recognizable room layout and signature furnishings |
| Furniture / icon | Single prop or coordinated icon set | 1:1; isolated, consistent scale and lighting |
| Asset pack | A named, organized group of assets | Agree on shared palette, outline weight, pixel size, and filename pattern |

## Brief to prompt

For each asset, capture only the details that affect the image:

1. Subject and defining features to preserve.
2. Requested view, pose, or camera angle.
3. Pixel scale and palette, using the style guide.
4. Background, composition, ratio, and output count.
5. Changes from any supplied reference; leave other identity-defining features intact.

Infer standard details when clear. Ask one focused question if a major choice remains ambiguous, such as whether a floor plan should be top-down or isometric. For other missing details, choose a reasonable default and proceed.

## Character sheets and turnarounds

- Use one main full-body character and only the views or poses requested.
- Keep face, hair, outfit, body proportions, palette, accessories, and pixel scale aligned across views.
- A practical layout is a large detailed hero sprite on the left with smaller front, side, and back views on the right.
- If the user asks for actions rather than a strict turnaround, use those actions instead of adding unrequested views.
- Avoid extra captions, stats, frames, UI, or decorative panels unless requested.

## Coordinated asset sets

- Reuse the approved style, outline treatment, palette, and lighting across related assets.
- For one recurring character, use an approved image as a reference for subsequent views when the generation tool supports references.
- For unrelated assets in a collection, keep the shared art direction while allowing each subject its own suitable colors.
- Generate one image at a time only when the user needs to approve a first asset before the rest; otherwise use the supported batch workflow.
- If exact identity or grid consistency is not achievable in one generated sheet, say so and offer separate images with shared references.

## Variations and revisions

- Change only the requested attribute: for example outfit, palette, expression, pose, or room decor.
- Make alternatives meaningfully distinct and label them in the response or filenames, not by adding text inside the art.
- When revising a supplied/generated image, preserve approved details and avoid unintended redesign.

## Organize and hand off

- Use a folder named for the project, then zero-padded numbering and descriptive filenames, such as `01-character-front.png` or `02-sunroom-interior.png`.
- Keep source references and final outputs separate. Never overwrite the source image.
- For a requested ZIP, include only the requested final assets and a short file list when useful.
- For requested resizing or compression, preserve the original, prefer a lossless format when practical, and report the final format, dimensions, and exact file size. If quality would visibly degrade to reach a target, explain the tradeoff before using a lossy format.
- Do not claim native Aseprite layers, editable `.aseprite` documents, animation, or sprite-atlas metadata unless a compatible tool actually produced them.
