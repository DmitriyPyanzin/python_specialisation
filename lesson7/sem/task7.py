# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import mkdir, replace, listdir, path


def create_dirs():
    if not path.isdir('image'):
        mkdir('image')
    if not path.isdir('table'):
        mkdir('table')
    if not path.isdir('media'):
        mkdir('media')
    if not path.isdir('docs'):
        mkdir('docs')


def sorted_files():
    create_dirs()
    for el in listdir():
        if el[-3:] in ['jpg', 'png']:
            replace(f'{el}', f'image/{el}')
        elif el[-3:] in ['xml']:
            replace(f'{el}', f'table/{el}')
        elif el[-3:] in ['mp3', 'avi']:
            replace(f'{el}', f'media/{el}')
        elif el[-3:] in ['txt', 'doc']:
            replace(f'{el}', f'docs/{el}')


if __name__ == '__main__':
    sorted_files()
