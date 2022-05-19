import random
import copy
import time


start_time = time.perf_counter()

DIR = [
    (-1, 0, 0, 0),
    (0, -1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]

n = int(input())
X = []
Y = []
board = []
R = []
score = 0


def calc_score(board):
  ret = 0
  for i in range(n):
    s = abs(board[i][0] - board[i][2]) * abs(board[i][1] - board[i][3])
    ret += 1 - (1 - min(R[i], s) / max(R[i], s))
  return ret


def is_vacant(x, bid):
  if not (0 <= x[0] <= x[2] < 10000) or not (0 <= x[1] <= x[3] < 10000):
    return False
  for i in range(n):
    if i == bid:
      continue
    if (x[2] < board[i][0] or board[i][2] < x[0]) or (x[3] < board[i][1] or board[i][3] < x[1]):
      continue
    return False
  return True


def random_exec():
  global score
  global board
  bid = random.randrange(n)
  did = random.randrange(4)
  x = [board[bid][i] + DIR[did][i] for i in range(4)]
  if is_vacant(x, bid):
    n_board = copy.deepcopy(board)
    n_board[bid] = x
    n_score = calc_score(n_board)
    if n_score > score:
      board = n_board
      score = n_score


for _ in range(n):
  x, y, r = list(map(int, input().split()))
  X.append(x)
  Y.append(y)
  board.append((x, y, x + 1, y + 1))
  R.append(r)
score = calc_score(board)

while time.perf_counter() - start_time < 5:
  random_exec()
for a, b, c, d in board:
  print(a, b, c, d)
