import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2022/07/input.txt') as f:
    lines = f.read().splitlines()


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.files = []
        self.subDirs = []
        self.parent = parent

    def checkout(self, newDir):
        for dir in self.subDirs:
            if dir.name == newDir:
                return dir

    def updateSize(self):
        size = 0
        for file in self.files:
            size += file[0]
        for subDir in self.subDirs:
            subDir.updateSize()
            size += subDir.size
        self.size = size


root = Directory('root')


# construct file system
curr = root
reading = False
seen = set()
path = ['root']
for line in lines:
    if reading:
        if tuple(path) in seen:
            continue
        if line.startswith('$'):
            reading = False
            seen.add(tuple(path))
        elif line.startswith('dir'):
            curr.subDirs.append(Directory(line[4:], parent=curr))
            continue
        else:
            size, name = line.split(' ')
            curr.files.append((int(size), name))
            continue

    if line == '$ ls':
        reading = True
    elif line == '$ cd ..':
        curr = curr.parent
        path.pop()
    elif line == '$ cd /':
        curr = root
        path = ['root']
    else:
        new = line[5:]
        path.append(new)
        curr = curr.checkout(new)

root.updateSize()


# Part 1
res = 0


def dfs(dir):
    global res
    if dir.size <= 100000:
        res += dir.size
    for subDir in dir.subDirs:
        dfs(subDir)


dfs(root)
print(res)

# Part 2
res = 30000000
neededSpace = root.size - 40000000


def dfs2(dir):
    global res
    if dir.size >= neededSpace:
        res = min(res, dir.size)
    for subDir in dir.subDirs:
        dfs2(subDir)


dfs2(root)
print(res)
