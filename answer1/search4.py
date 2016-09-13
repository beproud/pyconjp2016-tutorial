# coding: utf-8
import os


def search(target_path, keyword):
    if not os.path.exists(target_path):
        print('指定したパスが存在しません')
        return

    if not os.path.isdir(target_path):
        print('パスにはディレクトリを指定してください')
        return

    for path, dirnames, filenames in os.walk(target_path):
        for filename in filenames:
            filepath = os.path.join(path, filename)

            if not os.path.isdir(filepath):
                with open(filepath, encoding='utf-8') as f:
                    if keyword in f.read():
                        print(filename)


if __name__ == '__main__':
    search('notes', '雪')
