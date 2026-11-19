#!/usr/bin/env python3
"""Add meme captions to the GTA 6 getaway base image.

Top:    13 YEARS. TWO DELAYS. ONE GETAWAY.
Bottom: THE DRIVER'S A GHOST
White bold text, thick black outline, centred. Auto-fits to image width.
Writes meme-final.png (1024x1024) next to the base image.
"""
from PIL import Image, ImageDraw, ImageFont

BASE = "/home/hatch/workspace/makefun/entry-gta6-meme-x-01/assets/media-generation-gta6-getaway-base-0-ce9f2259-fd17-45e3-a13a-60b2d1654924.png"
OUT = "/home/hatch/workspace/makefun/entry-gta6-meme-x-01/meme-final.png"
FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

TOP = "13 YEARS. TWO DELAYS. ONE GETAWAY."
BOTTOM = "THE DRIVER'S A GHOST"

img = Image.open(BASE).convert("RGB")
W, H = img.size
S = W / 1024.0  # scale factor vs the 1024 design size
draw = ImageDraw.Draw(img)

MARGIN = int(36 * S)
MAX_W = W - 2 * MARGIN


def fit_font(text, start_size):
    size = start_size
    while size > 20:
        font = ImageFont.truetype(FONT_PATH, size)
        bbox = draw.textbbox((0, 0), text, font=font, stroke_width=max(2, size // 12))
        if bbox[2] - bbox[0] <= MAX_W:
            return font, size
        size -= 4
    return ImageFont.truetype(FONT_PATH, 20), 20


def draw_caption(text, y_top, start_size):
    font, size = fit_font(text, start_size)
    stroke = max(3, size // 11)
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2 - bbox[0]
    y = y_top - bbox[1]
    draw.text((x, y), text, font=font, fill="white",
              stroke_width=stroke, stroke_fill="black")
    return y + th


# Top caption over the sky.
draw_caption(TOP, int(28 * S), int(84 * S))
# Bottom caption over the hood/road.
draw_caption(BOTTOM, int(H - 118 * S), int(96 * S))

img.save(OUT, "PNG")
print("wrote", OUT, img.size)
