# Pikatang Pixel Art Style Guide

## Global style instructions

```
STYLE INSTRUCTIONS:
- Style: Pikatang (皮卡堂) hand-placed pixel art, cute, cozy, sweet
- Color: soft candy pastels (pink, mint, sky blue, butter yellow, cream) with warm wood tones; auto-match subject
- Ratio: character/pet 3:4, room/furniture 4:3, icon 1:1
- Resolution: 2K
- Text: none (no letters, numbers, labels, watermarks, UI frames)
- Consistency: asked before every batch (see anchor blocks)
```

## Style prefix (use at the start of every prompt)

```
Pikatang-style pixel art, hand-placed pixels on a strict visible pixel grid, crisp square pixels with no anti-aliasing and no blur. Clean 1-pixel outlines in a darkened tint of each shape's own color (never pure black). 2-3 tone cel shading with a small bright highlight on each form. Soft candy pastel palette (pink, mint, sky blue, butter yellow, cream) with warm wood accents. Cute, cozy, sweet, nostalgic casual-MMO game art.
```

## Character sprite style notes

Use these notes for characters and pets; room and item styles remain governed by their own templates. The supplied character examples share a cute game-avatar look: oversized head and eyes, compact body, expressive layered hair, and clothing/accessories with recognizable silhouettes.

- Make the pixel scale clearly visible. Use broad square-pixel clusters and stepped contours; avoid tiny texture pixels that make the result read as a smooth digital painting.
- Keep edges hard and shaded in a few discrete color steps. Avoid anti-aliasing, blur, airbrushed lighting, and smooth gradients.
- Use soft cream, pale yellow, pink, lilac, sky blue, and other subject-matched pastels. Keep enough value contrast for the face, outfit, and silhouette to read. Use blocky outlines about 1-2 coarse pixel units thick; this character-specific guidance overrides the thinner global outline. Outlines may be dark brown/plum or a strong palette-matched pink/lilac; do not default to pure black.
- Keep details, but group them into pixels: hair locks, bows, sleeves, skirt layers, shoes, and small props should be readable clusters rather than fine strands or realistic fabric texture.
- For reference sheets, use a large hero sprite at left and smaller full-body views at right when that matches the user's example. Front, side, and back views should clearly read as the same character.
- Style references may contain game UI, text, icons, creator marks, or watermarks. Treat those as source-image artifacts; do not reproduce them unless the user explicitly requests them.

## Subject templates

### A. Characters & pets (single sprite, ratio 3:4)

```
[STYLE PREFIX] A full-body Pikatang-style chibi character sprite, standing and facing slightly toward the viewer: [CHARACTER DESCRIPTION]. Use a large head, big expressive eyes, a compact small body, and readable hair, clothing, and accessories. Build the image from clearly visible chunky square-pixel clusters with stepped silhouettes and hard-edged 2-3 tone shading; pixels should remain obvious at normal viewing size. Use a soft pastel palette with a blocky outline about 1-2 coarse pixel units thick in a palette-matched dark brown, plum, or pink. Plain light background, one centered subject with generous margin.
```

For pets, use the same chunky pixel construction and palette-matched outlines. Add an egg only when the user requests one.

### Character reference sheet (ratio 3:4)

Use this when the user asks for a character sheet, turnaround, multiple angles, or provides a reference sheet layout. Keep the same character, outfit, proportions, colors, hair, and accessories consistent in every view.

```
[STYLE PREFIX] A portrait-format Pikatang-style pixel-art character reference sheet for [CHARACTER DESCRIPTION]. Place one large, detailed full-body chibi character in the left two-thirds, in [HERO POSE]. Place three smaller full-body views in a clean vertical column on the right: front, side, and back. Use simple pale panels and an optional thin pastel-pink or warm-gold frame. The character has a large head, expressive eyes, and a compact body. Construct hair, clothing, and accessories from visibly chunky square-pixel clusters with stepped edges, limited pastel color ramps, and hard-edged 2-3 tone shading. Preserve a clear low-resolution game-sprite look; do not soften the pixels into a smooth illustration. Keep every view fully visible and consistent. No labels or interface elements.
```

If the user asks for several poses instead of a strict turnaround, replace the side and back views with the requested actions. Do not add status bars, currency icons, dialogue bubbles, screenshots, watermarks, or text even when these appear in style references.

### B. Isometric rooms & furniture (ratio 4:3)

```
[STYLE PREFIX] An isometric cut-away pixel-art room in 2:1 pixel isometric projection, two walls and the floor visible, floating on a plain solid background: [ROOM THEME AND DESCRIPTION]. Densely and cozily furnished with small props (plants, books, string lights, rugs, windows with a sky view, small pets). Every object has the same pixel scale and outline treatment.
```

Single furniture piece: `A single isometric pixel-art furniture piece: [DESCRIPTION], on a plain solid light background, centered.`

### C. Item icons (ratio 1:1)

```
[STYLE PREFIX] A single small pixel-art item icon: [ITEM DESCRIPTION]. Glossy cute rendering with one bright highlight, warm saturated colors, slightly chubby simplified shape, sitting on a small plate or wooden board where natural. Centered on a plain solid white background with generous margin.
```

## Consistency anchor blocks

Ask the user which level applies before every batch.

**Must match**

```
Keep the exact same pixel size, outline color, palette, shading style and lighting direction as the reference image. Every image in this set must look like it came from the same game and the same artist.
```
Generate image 01 first, get approval, then pass it as `--reference` for the rest.

**Partly consistent**

```
Use the same pixel-art style, outline treatment and soft pastel mood as the rest of the set. Subjects, colors and details may differ.
```

**Allow variation**: no anchor block, shared style prefix only.

## Exclusions (append to every prompt)

```
No text, no letters, no numbers, no labels, no watermark, no signature, no UI frame, no border. No smooth gradients, no anti-aliasing, no blur, no 3D render, no photorealism, no vector look, no painterly brush strokes.
```

## Prompt rules

1. Describe the scene in full sentences; narrative description works better than keyword piles.
2. Always state background, ratio and the pixel grid explicitly.
3. Use the same style prefix for every image in a batch.
4. Characters and pets: one subject per image, centered, with margin (clean sprites for game asset use).
5. Rooms: name the theme and 4-6 signature props so the room reads clearly.
6. Reference mode: say what to keep (pose, subject) and what to change, and always restate the style prefix so the output converts to the Pikatang look.
7. Pikatang pixel density is a style target; the model approximates it, so judge by grid cleanliness and palette, not exact pixel counts.
