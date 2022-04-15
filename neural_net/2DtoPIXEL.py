"""
title：图片转换像素画
writer：山客
date：2021.8.1
"""

import tensorflow as tf


def DecodeImage(input_path: str, name: str):
    # 读取图片路径
    with tf.io.read_file(input_path) as f:
        image_data = tf.image.decode_image(f)

    output_path = "/photo_output/" + name
    with tf.io.write_file(output_path) as f:
        f


if __name__ == '__main__':
    cleanPhoto()