---
name: pikatang-pixel-art
description: Batch-generate Pikatang (皮卡堂) style pixel art for game assets and fan art collections — chibi characters and pets, isometric cut-away rooms and furniture, and small item icons (food, props). Uses the Gemini image API with a locked pixel-art style guide. Triggers on "皮卡堂风格", "皮卡堂像素图", "Pikatang pixel", "像素风角色/宠物/家具/房间/图标", "pixel fan art batch".
---

# Pikatang Pixel Art Generator

**Author: Yuzhuo Zhang**

Generates 5-10 images per batch in the Pikatang pixel-art style: soft candy pastels, clean dark-tinted outlines, no anti-aliasing, cozy and sweet. Three subject types share one style language: **characters & pets**, **isometric rooms & furniture**, **item icons**. Output is pure visuals with no text.

## Workflow

### Phase 1: Collect input (accept any of these)

| Mode | User provides | Skill does |
|---|---|---|
| Manual | One description per image | Expands each into a full prompt |
| List | A list of subjects (e.g. 8 pets, 6 rooms) | Builds one prompt per line |
| Reference + description | An image plus changes wanted | Passes the image with `--reference` and writes an adaptation prompt |

For each item, detect the subject type (character/pet, room/furniture, icon) and pick the matching template in `references/style-guide.md`. If a request mixes types, split it into separate images.
For character and pet requests, distinguish a single sprite from a character reference sheet. If the user asks for multiple views or supplies a sheet example, use the character-sheet template and match its layout. Keep the character style visibly chunky and pixel-built rather than softly illustrated.

### Phase 2: Ask the consistency level (every batch)

**Always ask this before writing prompts**, since the answer changes how strictly the style is anchored:

1. **Must match**: same pixel grid, outline color, palette and lighting across the set. Use the strict anchor block and reuse the first approved image as `--reference` for the rest.
2. **Partly consistent**: same style prefix, subjects and palettes may differ. Use the standard anchor block.
3. **Allow variation**: shared style prefix only, explore freely.

### Phase 3: Write prompts and confirm

1. Build each prompt from: style prefix + subject template + content description + anchor block (per consistency level) + exclusions.
2. Show all prompts (5-10) in a table: number, subject type, ratio, one-line summary.
3. **Wait for the user to confirm or edit** before generating anything.

### Phase 4: Generate

1. Create the folder `obsidian/09image/MMDD-topic/`.
2. Run `scripts/generate_image.py` once per image (command below). With "must match", generate image 01 first, let the user approve it, then pass it as `--reference` to the rest.
3. Name files `NN-subject.png`.
4. List the results and ask whether any should be regenerated or tweaked.

Images are not inserted into any document (game asset / fan art use).

## Defaults

| Setting | Value |
|---|---|
| Ratio | Auto by subject: character/pet 3:4, room/furniture 4:3, icon 1:1 (user can override) |
| Resolution | 2K |
| Text in image | None. Every prompt ends with the no-text exclusion |
| Color | Auto-match subject, Pikatang candy pastels by default |
| Model | `gemini-3-pro-image-preview` |

## API configuration

| Setting | Value |
|---|---|
| API URL | `https://generativelanguage.googleapis.com` |
| API key | Read from the `GEMINI_API_KEY` environment variable (never hardcode it in this file) |
| Model | `gemini-3-pro-image-preview` |

If `GEMINI_API_KEY` is not set, ask the user to set it or pass `--api-key`.

## Generate command

```bash
python3 scripts/generate_image.py \
  --prompt "<full prompt>" \
  --output "obsidian/09image/MMDD-topic/01-subject.png" \
  --aspect-ratio "3:4" \
  --resolution "2K" \
  --reference "references/style-refs/character-sprite.jpg"   # optional, repeatable
```

`--reference` accepts any local image (PNG/JPG/WebP). Bundled style anchors live in `references/style-refs/`:

| File | Use for |
|---|---|
| `character-sprite.jpg` | Chibi character / outfit sprite |
| `pet-egg-card.jpg` | Pets and eggs |
| `iso-room-bathroom.jpg` | Clean light isometric room |
| `iso-room-cozy.jpg` | Dense, warm isometric room |

## Usage examples

| User says | Action |
|---|---|
| "皮卡堂风格画 6 只森林宠物" | List mode, pet template, ask consistency, show 6 prompts |
| "做一个粉色兔子主题的房间" | Room template, 4:3 |
| "把这张图改成皮卡堂像素风" + image | Reference mode, adapt to style guide |
| "8 个食物图标: 火锅, 蛋糕, ..." | List mode, icon template, 1:1 |

See `references/style-guide.md` for the full style prefix, subject templates, anchor blocks and exclusions.
