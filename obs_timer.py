
"""
Script to output changing countdown to a text file for
use in an OBS scene.
"""

import time
import datetime
from dateutil.parser import parse
import argparse

parser = argparse.ArgumentParser(description="Start a countdown timer")
parser.add_argument('-t', dest='target', default=False, action="store_true", help="Countdown to target time")
parser.add_argument('TIME', type=str, help="Enter a floating number of minutes")
args = vars(parser.parse_args())

if args['target']:
    target = parse(args['TIME'])
else:
    dt = datetime.timedelta(minutes=float(args['TIME']))
    target = datetime.datetime.now()+dt

while datetime.datetime.now() < target:
    remaining = (target - datetime.datetime.now()).total_seconds()
    minutes = int(remaining / 60)
    seconds = int(remaining) % 60
    print(f"   {minutes}:{seconds:02d}", end='\r')
    with open('timer.txt', 'w') as f:
        f.write(f"{minutes}:{seconds:02d}")
    time.sleep(1)
