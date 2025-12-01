import datetime
import os
import argparse

# ./advent-of-code/make_files.py --year=XXXX

parser = argparse.ArgumentParser()
parser.add_argument("--year", type=str, help="The year argument", default=None)
args = parser.parse_args()
year = args.year or str(datetime.datetime.now().year)

current_directory = os.getcwd()

year_path = os.path.join(current_directory, "advent-of-code", year)

if not os.path.exists(year_path):
    os.makedirs(year_path)
    print(f"Created folder: {year}")

file_content = """
import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{{cwd}}/advent-of-code/{year}/{day}/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0

# Part 2
res2 = 0
"""

# Starting in 2025, only 12 days :(
for d in range(1, 13):
    day = "0" + str(d) if d < 10 else str(d)
    day_path = os.path.join(year_path, day)
    if not os.path.exists(day_path):
        os.makedirs(day_path)
        print(f"Created folder: {year} > {day} and associated files.")

    day_file = os.path.join(day_path, f"day{day}.py")
    input_file = os.path.join(day_path, "input.txt")
    example_file = os.path.join(day_path, "example.txt")
    if not os.path.exists(day_file):
        with open(day_file, "w") as f:
            f.write(file_content.format(year=year, day=day))
        open(input_file, "w").close()
        open(example_file, "w").close()

print("Done!")
