# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: convert images format
# Created: 2024.01.4
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/04    basic build success
# -----------------------------

import os
from PIL import Image


def convert_tga_to_jpg(input: str, output: str):
    if not os.path.exists(output):
        os.makedirs(output)

    for root, dirs, files in os.walk(input):
        for dir in dirs:
            for file in os.listdir(os.path.join(root, dir)):
                if file.lower().endswith('.tga'):
                    output_path = os.path.join(
                        output, dir, file.split('.')[0] + '.jpg')
                    
                    tga_image = Image.open(
                        os.path.join(root, dir, file)).convert('RGB')
                    tga_image.save(output_path, 'JPEG')

if __name__ == "__main__":
    input = "...."
    output = "..."

    convert_tga_to_jpg(input, output)
