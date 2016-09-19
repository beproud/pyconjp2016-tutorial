from PIL import Image


RATIO = 0.5
#: 縮小比率

with Image.open('./2016.png', 'r') as im:
    # 画像サイズを取得
    width, height = im.size

    # ``RATIO`` で縮小する
    resized = im.resize((
        int(RATIO * width),
        int(RATIO * height),
    ))

    # 縮小された画像 (``resized``) を保存する
    resized.save('./resized-2016.png')
