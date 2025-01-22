
import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2021/12/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0

# Part 2
res2 = 0
