import math


def factorization(n):
  tmp = n
  ret = []
  for i in range(2, math.floor(math.pow(n, 1 / 2)) + 1):
    while tmp % i == 0:
      tmp //= i
      ret.append(i)
  if tmp > 1:
    ret.append(tmp)
  return ret
