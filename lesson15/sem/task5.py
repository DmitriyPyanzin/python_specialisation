import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Принимает строку с датой')
parser.add_argument('-cnt', type=str, default='1')
parser.add_argument('-wd', type=str, default=str(datetime.now().weekday()))
parser.add_argument('-m', type=str, default=str(datetime.now().month))

args = parser.parse_args()
print(args)
# (f'{args.cnt}-{args.wd}-{args.m}')