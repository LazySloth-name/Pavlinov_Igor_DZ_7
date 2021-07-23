# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
import os
from shutil import copytree


def copy_dir():
    source_dir = 'my_project'  # каталог
    dir_name = 'templates'     # имя искомой папки

    for root, dirs, files in os.walk(source_dir):
        if root.find(dir_name) > 0 and len(files) == 0:
            copytree(os.path.join(root), dir_name, dirs_exist_ok=True)

if __name__ == '__main__':
    copy_dir()