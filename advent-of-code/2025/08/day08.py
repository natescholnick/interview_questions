
import os
import sys
from collections import defaultdict, deque, Counter
import re
import heapq
import math
import bisect
import numpy as np

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2025/08/input.txt") as f:
    lines = f.read().splitlines()

# Part 1
res = 0

# Part 2
res2 = 0
