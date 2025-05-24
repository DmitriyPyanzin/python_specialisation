import os
import logging
import collections
import argparse

FileInfo = collections.namedtuple('FileInfo', ['name', 'ext', 'is_dir', 'parent_dir'])
logging.basicConfig(filename='task5.log', level=logging.INFO, style='{', format='{asctime} - {message}')


def collect(dir_path):
    if not os.path.isdir(dir_path):
        raise ValueError(f'Путь {dir_path} не является директорией')

    parent_dir = os.path.basename(os.path.abspath(dir_path))

    for el in os.listdir(dir_path):
        el_path = os.path.join(dir_path, el)
        if os.path.isdir(el_path):
            file_info = FileInfo(name=el, ext=None, is_dir=True, parent_dir=parent_dir)
        else:
            name, ext = os.path.splitext(el)
            file_info = FileInfo(name=name, ext=ext.lstrip('.'), is_dir=False, parent_dir=parent_dir)

        logging.info(f'{file_info.name} | {file_info.ext if file_info.ext else "N/A"} | '
                     f'{"DIR" if file_info.is_dir else "FILE"} | {file_info.parent_dir}')


def main():
    parser = argparse.ArgumentParser(description='Сбор информации и логирование')
    parser.add_argument('dir', type=str, help='Путь до директории')
    args = parser.parse_args()
    dir_path = args.dir

    try:
        collect(dir_path)
        print(f'Содержимое директории {dir_path} записана в файл task5.log')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
