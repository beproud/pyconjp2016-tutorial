import os


def add_file_suffix(path, suffix):
    """ ファイルパス path のファイル名に、 suffix を付けて返す

    >>> add_file_suffix('./path/to/image.jpg', 'thumb')
    './path/to/image_thumb.jpg'
    """
    root, ext = os.path.splitext(path)
    return root + '_' + suffix + ext


def has_target_extname(path, ext_names):
    """ ファイル path の拡張子が ext_names のリスト内にある場合Trueを返す

    >>> has_target_extname('./images/2016.jp', ['jpg', 'png', 'gif'])
    True
    """
    return os.path.splitext(path)[1].lstrip('.') in ext_names


def dir_to_files(root_dir_path):
    """ root_dir_path 以下すべてのファイルパスを返す

    >>> dir_to_files('./images')
    ./images/2016.jpg
    ./images/2016.png
    ./images/trip/alps.jpg
    ./images/trip/sky.jpg
    """
    for dir_path, dirs, files in os.walk(root_dir_path):
        for file in files:
            yield os.path.join(dir_path, file)
