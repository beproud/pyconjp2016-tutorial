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


def main(root_dir_path, extname):
    """ ディレクトリーのパスを受け取り、ディレクトリー以下すべての画像を縮小して同じディレクトリーに保存する
    ただし拡張子 extname を持つ画像だけを対象にする
    """
    for dir_path, dirs, files in os.walk(root_dir_path):
        for file in files:
            if file.endswith(extname):
                image_path = os.path.join(dir_path, file)
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
    path = sys.argv[1]
    extname = sys.argv[2]
    main(path, extname)
