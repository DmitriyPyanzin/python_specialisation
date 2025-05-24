import datetime


def display_current():
    now = datetime.datetime.now()
    format_date = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_num = now.isoweekday()

    print(f'Текущая дата и время: {format_date}')
    print(f'День недели: {day_of_week}')
    print(f'Номер недели: {week_num}')


if __name__ == '__main__':
    display_current()
    