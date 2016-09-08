import argparse

from .pathutil import dir_to_files
from .pathutil import has_target_extname
from .thumbnail import thumbnail


def main():
    """ 画像縮小コマンド

    画像の縮小::

        $ thumbnailer ./images/2016.png

    縮尺指定での縮小::

        $ thumbnailer -s 0.5 ./images/2016.png

    ディレクトリー指定の縮小::

        $ thumbnailer -r ./images/
    """
    parser = argparse.ArgumentParser(description='画像のサムネイルを生成するコマンド')
    parser.add_argument('paths', nargs='+', help='対象の画像 / ディレクトリーのパス')
    parser.add_argument('-s', '--size', type=float, default=0.5,
                        help='返還後の画像の縮尺。 0.5 など小数で指定')
    parser.add_argument('-r', '--recursive', action='store_true', default=False,
                        help='ディレクトリーを指定して再帰的に処理する場合指定')
    parser.add_argument('-t', '--type', type=str, nargs='+', default=['jpg', 'png', 'gif'],
                        help='処理の対象になる画像ファイルの種類')
    args = parser.parse_args()

    # コマンドからは画像のパスを直接指定するか、ディレクトリーで指定される
    # 指定方法はともかくとして「実行対象の画像パスのリスト」(target_image_paths) に一旦変換する
    target_image_paths = []
    if args.recursive:
        # recursive オプションがある場合はディレクトリー配下のファイルパスを一覧をとる
        for dir_path in args.paths:
            for image_path in dir_to_files(dir_path):
                target_image_paths.append(image_path)
    else:
        # オプション無しの場合は args.paths の値を画像のパスとする
        target_image_paths = args.paths

    for image_path in target_image_paths:
        # 要らない拡張子のファイルは無視する
        if has_target_extname(image_path, args.type):
            thumbnail_image_path = thumbnail(image_path, thumbnail_ratio=args.size)
            print(thumbnail_image_path)
