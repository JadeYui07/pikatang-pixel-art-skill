---
name: pikatang-pixel-art
description: Create Pikatang-inspired pixel-art assets from text or image references, including characters, character sheets, pets, houses, interiors, furniture, and icons. Use for single images, coordinated asset sets, and visual variations.
---

# Pikatang Pixel Asset Workshop

**Author: JadeYui07**

Help the user plan, generate, revise, and organize cozy Pikatang-inspired pixel art. Use a visible chunky pixel grid, stepped silhouettes, compact chibi proportions where appropriate, and warm candy pastels. Choose only the workflow relevant to the request; this is an image-generation skill, not an Aseprite editor or animation system.

## Choose a workflow

Read [references/workbench.md](references/workbench.md) when the request involves choosing an asset type, making a coordinated set, a character sheet, variations, or packaging outputs. If the user wants SpriteCook, read [references/spritecook.md](references/spritecook.md).

For requested native-grid cleanup, read [references/pixel-cleanup.md](references/pixel-cleanup.md). For Aseprite editing or export, read [references/aseprite.md](references/aseprite.md). These are optional local steps; do not run post-processing merely because an image looks pixelated. Perfect Pixel is separately installed, and transparent inputs are not supported by the included adapter.

- **Character:** single full-body avatar, character sheet, turnaround, or requested poses.
- **Pet:** single pet sprite or a requested set of views/expressions.
- **House:** exterior view or architectural cutaway, following the user's reference and camera angle.
- **Interior:** isometric room, top-down plan, or cutaway. Infer from the reference; ask only if the camera choice materially changes the result.
- **Furniture / icon:** one isolated prop or a coordinated set.
- **Reference adaptation:** keep the subject details the user identifies, and change only the requested style or attributes. Treat embedded UI, captions, and watermarks as reference artifacts unless asked to include them.
- **Asset pack:** plan consistent style, palette, naming, and ratios across multiple requested assets.

## Run the request

1. Infer the asset type, composition, and ratio from the user's request and references. Use sensible defaults rather than asking for choices the user has already implied. Ask one concise question only when a missing choice would materially change the output.
2. For a set, maintain identity and visual continuity where needed. Default unrelated assets to a shared style and palette; ask whether strict matching is required only when that distinction matters. Do not require prompt approval unless the user asks to review prompts first.
3. Build prompts using the relevant template in [references/style-guide.md](references/style-guide.md). For characters, make pixels visibly coarse and block-built; retain readable clothing and silhouette details without smoothing into a digital painting.
4. Generate or edit with the image-generation capability available in the current environment. If SpriteCook tools are connected and the user wants to use them, follow [references/spritecook.md](references/spritecook.md). When the user specifically wants the bundled Gemini API script, follow the command below. Never claim to have run an unavailable generator.
5. Present results clearly and offer focused revisions. Do not silently change identity-defining details between views.
6. For requested asset handoff, use consistent descriptive filenames and group files in a project folder. Resize, convert, or compress only when requested; preserve originals and confirm the resulting dimensions and file sizes when those operations are available.

## Gemini API script

The bundled script uses Python's standard library and requires a Gemini API key in `GEMINI_API_KEY` (or `--api-key`). Never write the key into repository files or generated prompts.

```bash
python3 scripts/generate_image.py \
  --prompt "<complete prompt>" \
  --output "outputs/<project-name>/01-<asset-name>.png" \
  --aspect-ratio "3:4" \
  --resolution "2K" \
  --reference "references/style-refs/character-sprite.jpg"
```

Repeat `--reference` for additional local images. Bundled anchors: `character-sprite.jpg` (avatars), `pet-egg-card.jpg` (pets), `iso-room-bathroom.jpg` (bright interiors), and `iso-room-cozy.jpg` (warm interiors). The script's default model is documented in its help and can be overridden with `--model`.

## Defaults

- Character and pet sprites: portrait 3:4, one clear subject, plain background.
- Rooms and house scenes: 4:3 unless the reference or requested framing suggests otherwise.
- Furniture and item icons: square 1:1, isolated on a plain background.
- Resolution: 2K when supported; use the available generator's nearest option otherwise.
- No text, watermarks, signatures, or game UI unless requested.
- For a character turnaround, use a large detailed full-body hero on the left and smaller front/side/back views on the right when that matches the request or reference.

## Example requests

- “做一张角色全身设定图，左侧主立绘，右边正面、侧面和背面。”
- “把这只宠物做成皮卡堂粗像素风，再给两种表情。”
- “按这张房子参考图，分别做外观和内部装饰。”
- “把这 6 个家具图标统一成一套，做成 1:1 白底素材。”
- “把这组 PNG 整理成有序命名的 ZIP，并压到 1 MB 以内。”
