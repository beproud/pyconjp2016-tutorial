from PIL import Image

from .pathutil import add_file_suffix


def thumbnail(image_path, thumbnail_ratio=0.5, suffix='thumb'):
    """ 画像のパス image_path を受け取り、 thumbnail_ratio に指定された引数で縮小する。
    変換後のファイル名を返す。
    """
    thumbnail_image_path = add_file_suffix(image_path, suffix)

    with Image.open(image_path, 'r') as im:
        width, height = im.size

        thumbnail_image = im.resize((
            int(thumbnail_ratio * width),
            int(thumbnail_ratio * height),
        ))

        thumbnail_image.save(thumbnail_image_path)
    return thumbnail_image_path
