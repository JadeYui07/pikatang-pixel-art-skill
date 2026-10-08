# Aseprite handoff

Use when the user wants to edit generated assets in Aseprite or export an existing Aseprite document. Aseprite must be installed separately. This skill does not bundle Aseprite, include an Aseprite plugin, or provide an automatic layer/animation generator.

## Practical workflow

1. Generate a single isolated asset with clear coarse pixels. Keep the generated source.
2. If requested, use [optional pixel cleanup](pixel-cleanup.md) to obtain a small native-grid PNG. Skip that adapter for transparent images; preserve alpha.
3. In Aseprite, use **File > Open** for the PNG, then **File > Save As** to create a new `.aseprite` document. A flattened PNG starts as a single image layer. It cannot recover separate hair, clothing or background layers automatically.
4. Zoom in to edit individual pixels. Check the silhouette, eye highlights, color count and stray pixels. Split components into layers manually when useful.
5. For animation, build and edit frames in Aseprite, keep canvas size and character placement consistent, then check timing and continuity. A sheet showing different characters or views is not automatically an animation.
6. Export PNG for a still, GIF for an existing animation, or a sprite sheet plus JSON for game use. Keep `.aseprite` as the editable master.

## Existing sheets

Use **File > Import Sprite Sheet** only for a regular frame grid whose cell dimensions, spacing and order are known. The current decorative item and character collection sheets are showcase layouts; separate/crop their assets before using them as individual sprites. Importing an arbitrary collage does not identify objects automatically.

## Optional command-line handoff

Only use a verified, user-installed Aseprite executable. If `aseprite` is not on PATH, obtain its actual location. Choose new output names; the CLI can overwrite files.

```bash
# Wrap a still PNG in an editable Aseprite document (still one layer/frame).
aseprite -b sprite-native.png --save-as sprite.aseprite

# Export frames that already exist in an edited document.
aseprite -b animated.aseprite --sheet output/sheet.png --data output/sheet.json --format json-array

# Export an existing animation as GIF.
aseprite -b animated.aseprite --save-as output/animation.gif
```

Do not claim `.aseprite`, separated layers or animation exports were produced unless the installed tool actually created them. No GitHub credentials are needed for local editing or export.

Sources: [Aseprite files](https://www.aseprite.org/docs/files/), [sprite sheets](https://www.aseprite.org/docs/sprite-sheet/), [CLI](https://www.aseprite.org/docs/cli/).
