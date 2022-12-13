from collections import defaultdict
import os

cwd = os.getcwd()

with open(f'{cwd}/advent-of-code/2021/4/input.txt') as f:
    lines = f.read().splitlines()

draws = [int(x) for x in lines[0].split(',')]
boards = []
for i in range(2, len(lines), 6):
    boards.append([])
    for j in range(5):
        boards[-1].append([int(x) for x in lines[i+j].split(' ')])

sol = ['X', 'X', 'X', 'X', 'X']


def scoreBoard(board, factor):
    total = 0
    for row in board:
        for ele in row:
            if ele != 'X':
                total += ele
    return factor * total


# Part 1
def findWinnerScore():
    for num in draws:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = 'X'
                        if board[i] == sol or [board[x][j] for x in range(5)] == sol:
                            return scoreBoard(board, num)


print(findWinnerScore())


# Part 2
def findLoserScore():
    won = 0
    for num in draws:
        for board in boards:
            if board[0][0] == 'W':
                continue
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = 'X'
                        if board[i] == sol or [board[x][j] for x in range(5)] == sol:
                            if won == len(boards) - 1:
                                return scoreBoard(board, num)
                            board[0][0] = 'W'
                            won += 1


print(findLoserScore())
