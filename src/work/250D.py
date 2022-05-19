import math
import bisect


def eratosthenes(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, math.floor(math.pow(n, 1 / 2) + 1)):
    if not is_prime[i]:
      continue
    tmp = 2 * i
    while tmp <= n:
      is_prime[tmp] = False
      tmp += i
  return [i for i in range(n + 1) if is_prime[i]]


P = eratosthenes(10 ** 7)
N = int(input())

ans = 0
for i, q in enumerate(P):
  if q ** 3 > N:
    print(ans)
    exit()
  mp = math.floor(N / (q ** 3))
  ans += max(min(bisect.bisect_right(P, mp), i), 0)
  # print(q, max(min(bisect.bisect_right(P, mp), i), 0))
