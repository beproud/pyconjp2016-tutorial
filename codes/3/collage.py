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

i = 0
for grid_x in range(0, 1600, 800):
    for grid_y in range(0, 900, 450):
        with Image.open(target_image_paths[i], 'r') as im:
            resized = im.resize((800, 450))
            collage_im.paste(resized, (grid_x, grid_y))
        i += 1


collage_im.save(COLLAGE_IMAGE_PATH)
