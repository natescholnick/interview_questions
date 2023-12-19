import os
from collections import defaultdict, deque, Counter
import re
import heapq

cwd = os.getcwd()

with open(f"{cwd}/advent-of-code/2023/19/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
jobslist = {}    
parts = []
workflow = True
for line in lines:
    if len(line) == 0:
        workflow = False
        continue
    if workflow:
        name, evals = line.rstrip('}').split('{')
        evals = evals.split(',')
        jobslist[name] = evals
    else:
        parts.append(eval(re.sub(r'([a-z])', r"'\1'", line.replace('=', ':'))))
        

def evalPart(part, job):
    if job == 'R':
        return 0
    if job == 'A':
        return sum(part.values())
    for check in jobslist[job][:-1]:
        eq, nxt = check.split(':')
        x, m, a, s = part['x'], part['m'], part['a'], part['s']
        if eval(eq):
            return evalPart(part, nxt)
    return evalPart(part, jobslist[job][-1])

res = 0
for part in parts:
    res += evalPart(part, 'in')

print(res)

# Part 2
res2 = 0

def copyRanges(ranges):
    return {
        'x': [ranges['x'][0], ranges['x'][1]],
        'm': [ranges['m'][0], ranges['m'][1]],
        'a': [ranges['a'][0], ranges['a'][1]],
        's': [ranges['s'][0], ranges['s'][1]]
    }

def dfs(job, ranges):
    global res2
    if job == 'R':
        return
    if job == 'A':
        combins = 1
        for r in ranges.values():
            combins *= (r[1] - r[0] + 1)
        res2 += combins
        return
    for check in jobslist[job][:-1]:
        eq, nxt = check.split(':')
        cat, op, val = eq[0], eq[1], int(eq[2:])
        if op == '<':
            if ranges[cat][0] >= val:
                continue
            prev = ranges[cat][1]
            ranges[cat][1] = min(prev, val - 1) # subset of inputs that qualify for this next job
            dfs(nxt, copyRanges(ranges))
            if prev < val: # if previous restrictions already qualify for a certain check, we'll never go to the next check
                return
            ranges[cat][1] = prev
            ranges[cat][0] = val # subset of inputs that go to the next check
        else:
            if ranges[cat][1] <= val:
                continue
            prev = ranges[cat][0]
            ranges[cat][0] = max(prev, val + 1)
            dfs(nxt, copyRanges(ranges))
            if prev > val:
                return
            ranges[cat][0] = prev
            ranges[cat][1] = val

    dfs(jobslist[job][-1], copyRanges(ranges))


dfs('in', {'x':[1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})

print(res2)
