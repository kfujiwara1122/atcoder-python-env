import math
from collections import defaultdict


def factorization(n):
  tmp = n
  ret = []
  for i in range(2, math.floor(math.pow(n, 1 / 2)) + 1):
    while tmp % i == 0:
      tmp //= i
      ret.append(i)
  return ret


def cnt(n):
  l = factorization(n)
  d = defaultdict(int)
  for i in l:
    d[i] += 1
  ret = 1
  for _, v in d.items():
    ret *= (v + 1)
  return ret


tmp = 0
for i in range(1, 10 ** 6):
  tmp += i
  if cnt(tmp) > 500:
    print(tmp)
    exit()
