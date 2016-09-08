import os
from PIL import Image


RATIO = 0.5
# 読み込み対象のディレクトリー
TARGET_DIR = './resize/'

for filename in os.listdir(TARGET_DIR):
    # 読み込む画像のファイルパス (./images/alps.jpg)
    target_image_path = os.path.join(TARGET_DIR, filename)
    # 書き込む画像のファイルパス (./images/resized_alps.jpg)
    resized_image_name = 'resized_' + filename
    resized_image_path = os.path.join(TARGET_DIR, resized_image_name)

    with Image.open(target_image_path, 'r') as im:
        # 画像サイズを取得
        width, height = im.size

        # ``RATIO`` で縮小する
        resized = im.resize((
            int(RATIO * width),
            int(RATIO * height),
        ))

        # 縮小された画像 (``resized``) を保存する
        resized.save(resized_image_path)
