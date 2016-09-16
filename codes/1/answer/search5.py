# coding: utf-8
import os
import re

NUM_CHARS = 5


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
                    text = f.read().replace('\n', '')
                    match = re.search(keyword, text)
                    if match:
                        print('{filepath}: {prefix}\033[92m{main}\033[0m{suffix}'.format(
                            filepath=filepath,
                            prefix=text[match.start() - NUM_CHARS:match.start()],
                            main=text[match.start():match.end()],
                            suffix=text[match.end():match.end() + NUM_CHARS]
                        ))


if __name__ == '__main__':
    search('../notes', '雪')
