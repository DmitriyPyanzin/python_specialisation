import datetime


def future(now_day):
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days=now_day)
    format_future = future_date.strftime("%Y-%m-%d")
    return format_future

if __name__ == '__main__':
    days = 100
    print(f'{days} дней до {future(days)}')
