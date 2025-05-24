import argparse


def pars():
    parser = argparse.ArgumentParser(description='Процесс вывода строки определённое количество раз')
    parser.add_argument('num', type=int, help='Число для ввода')
    parser.add_argument('text', type=str, help='Текст для ввода')
    parser.add_argument('--verbose', action='store_true', help='Дополнительная информация')
    parser.add_argument('repeat', type=int, default=1, help='Количество повторений')

    args = parser.parse_args()
    if args.verbose:
        print(f'Полученные данные: number={args.num}, text={args.text}, repeat={args.repeat}')
        print(f'Число: {args.num}, Строка: {args.text * args.repeat}')

if __name__ == '__main__':
    pars()
