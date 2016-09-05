import os
import sys

from PIL import Image

THUMBNAIL_RATIO = 0.5


def add_file_suffix(path, suffix):
    """ ファイルパス path のファイル名に、 suffix を付けて返す

    >>> add_file_suffix('./path/to/image.jpg', 'thumb')
    './path/to/image_thumb.jpg'
    """
    root, ext = os.path.splitext(path)
    return root + '_' + suffix + ext


def main(image_paths):
    """ 画像パスのリスト image_paths を縮小して同じディレクトリーに保存する
    """
    for image_path in image_paths:
        thumbnail_image_path = add_file_suffix(image_path, 'thumb')

        with Image.open(image_path, 'r') as im:
            width, height = im.size

            thumbnail_image = im.resize((
                int(THUMBNAIL_RATIO * width),
                int(THUMBNAIL_RATIO * height),
            ))

            thumbnail_image.save(thumbnail_image_path)
            print(thumbnail_image_path)


if __name__ == '__main__':
    paths = sys.argv[1:]
    main(paths)
