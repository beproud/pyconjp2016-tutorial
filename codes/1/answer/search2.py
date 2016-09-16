# coding: utf-8
import os


def search(target_path, keyword):
    if not os.path.isdir(target_path):
        print('パスにはディレクトリを指定してください')
        return

    for filename in os.listdir(target_path):
        filepath = os.path.join(target_path, filename)

        if not os.path.isdir(filepath):
            with open(filepath, encoding='utf-8') as f:
                if keyword in f.read():
                    print(filename)


if __name__ == '__main__':
    search('../notes', '雪')
