L = dict()
L[1] = 1
m = 0
ans = -1


def dfs(n):
  # print(n)
  global L
  global ans
  global m
  if n in L:
    return L[n]
  ret = -1
  if n % 2:
    ret = dfs(3 * n + 1) + 1
  else:
    ret = dfs(n // 2) + 1
  L[n] = ret
  # print("  ", ret)
  if ret > m:
    m = ret
    ans = n
  return ret


for i in range(1, 10 ** 6):
  dfs(i)
print(ans, m)
