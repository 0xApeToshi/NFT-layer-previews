import os
import random

from PIL import Image

from config import FOLDERS, HEIGHT, N_SAMPLES, SEED, WIDTH


if __name__ == "__main__":
    random.seed(SEED)

    if "output" not in os.listdir():
        os.mkdir("output")

    for tokenId in range(N_SAMPLES):
        subfolder = os.listdir(f"layers/{FOLDERS[0]}")
        if ".DS_Store" in subfolder:
            subfolder.remove(".DS_Store")
        img_name = random.choice(subfolder)

        base_layer = Image.open(
            f"layers/{FOLDERS[0]}/{img_name}").convert("RGBA").resize((WIDTH, HEIGHT), Image.ANTIALIAS)

        for f in FOLDERS[1:]:
            subfolder = os.listdir(f"layers/{f}")
            if ".DS_Store" in subfolder:
                subfolder.remove(".DS_Store")
            img_name = random.choice(subfolder)

            next_layer = Image.open(
                f"layers/{f}/{img_name}").convert("RGBA").resize((WIDTH, HEIGHT), Image.ANTIALIAS)

            base_layer.paste(next_layer, (0, 0), next_layer)

        base_layer.save(f"output/sample_{tokenId}.png", "PNG")
