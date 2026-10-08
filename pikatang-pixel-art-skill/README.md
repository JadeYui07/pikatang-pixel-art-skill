<div align="right">[English](#english) | [简体中文](#简体中文)</div>

# Pikatang Pixel Art Generator

**Author: Yuzhuo Zhang**

## English

A Codex skill for creating cozy, colorful Pikatang-inspired pixel art from a written brief or image references. It supports chibi character sprites and turnarounds, pets, isometric rooms and furniture, and small item icons.

### Character style

Character art uses a clear low-resolution game-sprite look: chunky square-pixel clusters, stepped silhouettes, compact chibi proportions, expressive faces, and soft pastel palettes. A character reference sheet can place a detailed full-body hero sprite on the left with front, side, and back views on the right. Text, watermarks, and game UI from reference screenshots are excluded unless requested.

### Examples

These AI-generated examples were made while trying the skill. Original reference photos and screenshots are not included.

| House | Garden room | Pet character sheet |
|---|---|---|
| ![Pixel-art house](examples/pikatang-house-pixel.png) | ![Pixel-art garden sunroom](examples/pikatang-garden-sunroom.png) | ![Chinchilla character sheet](examples/chinchilla-character-sheet.png) |

| Bride character sheet | Blue-gown character sheet |
|---|---|
| ![Bride character sheet](examples/bride-character-sheet.png) | ![Blue gown character sheet](examples/blue-gown-character-sheet.png) |

### Install

Copy this repository folder into your Codex skills directory:

```text
~/.codex/skills/pikatang-pixel-art/
```

If you use a custom `CODEX_HOME`, install it under `$CODEX_HOME/skills/pikatang-pixel-art/`. The skill is available to Codex on the next turn.

### Generate with the bundled Gemini script

Requirements: Python 3 and a Gemini API key. The script uses Python's standard library.

Set the key in your shell (do not commit it):

```bash
export GEMINI_API_KEY="your-api-key"
```

Then run from the skill directory:

```bash
python3 scripts/generate_image.py \
  --prompt "A cozy pastel pixel-art room with a sunny window and plants" \
  --output "output/room.png" \
  --aspect-ratio "4:3" \
  --resolution "2K" \
  --reference "references/style-refs/iso-room-cozy.jpg"
```

Pass `--reference` more than once to include multiple local reference images. The default model is configured in `scripts/generate_image.py` and can be changed with `--model`.

### Typical workflow

1. Describe the subject or provide an image reference.
2. Choose how closely a set should match in style.
3. Review and confirm the prompts.
4. Generate images and refine any that need another pass.

## 简体中文

这是一个 Codex skill，可根据文字描述或图片参考生成温暖、可爱的皮卡堂风格像素图。支持 Q 版人物立绘和多角度设定图、宠物、等距房间与家具，以及小物件图标。

### 人物风格

人物图采用清晰的低分辨率游戏角色风格：明显的方块像素簇、阶梯轮廓、紧凑的 Q 版比例、富有表现力的面部，以及柔和的粉彩配色。角色设定图可以采用左侧精细全身主立绘、右侧正面/侧面/背面视图的布局。参考截图中的文字、水印和游戏 UI 默认不带入生成结果。

### 示例

以下为使用该 skill 测试时生成的 AI 示例图；未包含原始人物照片或参考截图。

| 房屋 | 花园房间 | 宠物角色设定图 |
|---|---|---|
| ![像素风房屋](examples/pikatang-house-pixel.png) | ![像素风花园阳光房](examples/pikatang-garden-sunroom.png) | ![龙猫角色设定图](examples/chinchilla-character-sheet.png) |

| 新娘角色设定图 | 冰蓝礼服角色设定图 |
|---|---|
| ![新娘角色设定图](examples/bride-character-sheet.png) | ![冰蓝礼服角色设定图](examples/blue-gown-character-sheet.png) |

### 安装

将此仓库目录复制到 Codex skills 目录：

```text
~/.codex/skills/pikatang-pixel-art/
```

如果使用自定义 `CODEX_HOME`，请安装到 `$CODEX_HOME/skills/pikatang-pixel-art/`。Codex 会在下一轮识别该 skill。

### 使用内置 Gemini 脚本生成

需要 Python 3 和 Gemini API key；脚本使用 Python 标准库，无需额外安装 Python 依赖。

在终端设置 API key（不要提交到 GitHub）：

```bash
export GEMINI_API_KEY="your-api-key"
```

然后在 skill 目录中运行：

```bash
python3 scripts/generate_image.py \
  --prompt "阳光窗边、摆满绿植的温馨粉彩像素房间" \
  --output "output/room.png" \
  --aspect-ratio "4:3" \
  --resolution "2K" \
  --reference "references/style-refs/iso-room-cozy.jpg"
```

可以重复传入 `--reference` 来提供多张本地参考图。默认模型配置在 `scripts/generate_image.py` 中，也可用 `--model` 指定其他模型。

### 常见流程

1. 描述主题，或提供图片参考。
2. 选择一组图片需要保持多大程度的风格一致。
3. 检查并确认生成提示词。
4. 生成图片，并继续调整需要重做的结果。

## Attribution / 署名

Created by **Yuzhuo Zhang**.

## License / 许可证

No license has been selected yet. Add a license before redistributing or accepting contributions.

尚未选择开源许可证。公开分发或接受贡献前，请先添加合适的许可证。
