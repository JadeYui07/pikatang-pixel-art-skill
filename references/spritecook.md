# SpriteCook Compatibility

Use this as an optional generation backend only when the user asks to use SpriteCook and SpriteCook's MCP tools or API are configured in the current environment. The skill supplies the Pikatang art direction and helps plan assets; SpriteCook performs the connected generation, editing, animation, or export. A prompt alone does not connect SpriteCook.

## Map the workbench brief

- For a crisp game sprite, set pixel mode on. Enable pixel-perfect processing when the user wants grid-aligned output and the connected tool exposes that setting.
- Use transparent background for isolated game sprites, icons, and props; use white or included background for concept art or room scenes as requested.
- Use the palette, dimensions, variation count, style theme, and reference/edit options only when exposed by the connected tool. Keep reference asset IDs local to the user's project if later edits, matching assets, or animation need them.
- For a coordinated pack, create one approved style anchor and reuse it as the reference for related assets. Preserve asset identity and palette while prompting changes.
- For animation, use a generated or imported source asset and specify the action, view, and frame count. Do not promise exact frame alignment or a game-engine-ready animation until the returned sheet/settings are inspected.
- For game handoff, use SpriteCook's available exports. Verify transparency, frame order, dimensions, and output format before calling an asset game-ready.

## API notes

The public API currently documents prompt-based generation and animation, asset import, reference/edit asset IDs, pixel settings, background modes, dimensions, and variations. API limits, available models, and pricing can change. If using the API directly, consult the current [SpriteCook API documentation](https://www.spritecook.ai/api-docs) instead of hardcoding model names or credit costs.

API usage may consume account credits and send prompts or reference images to SpriteCook. Use it only for a user-requested SpriteCook workflow, keep API keys out of files and output, and report any relevant credit or generation limits.

## Fallback

If SpriteCook is not connected, say so plainly and use an available image-generation capability or the bundled Gemini script. Do not claim that the bundled Gemini script creates animations, editable SpriteCook assets, or SpriteCook project files.
