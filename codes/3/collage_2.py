import itertools
import os

from PIL import Image


# コラージュ元画像のディレクトリー
TARGET_DIR = './collage/'
# 書き出し画像のパス
COLLAGE_IMAGE_PATH = './collage/collage.jpg'


target_image_paths = []
# コラージュ元画像のパスをリストにする
for filename in os.listdir(TARGET_DIR):
    target_image_path = os.path.join(TARGET_DIR, filename)
    target_image_paths.append(target_image_path)


collage_im = Image.new('RGB', size=(1600, 900))

for (grid_x, grid_y), path in zip(itertools.product(range(0, 1600, 800), range(0, 900, 450)),
                                  target_image_paths):
    with Image.open(path, 'r') as im:
        resized = im.resize((800, 450))
        collage_im.paste(resized, (grid_x, grid_y))


collage_im.save(COLLAGE_IMAGE_PATH)
