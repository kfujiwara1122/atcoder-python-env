import copy


N, MOD = list(map(int, input().split()))
ans = 0
fact = [1] * (N + 1)
rfact = [1] * (N + 1)
r = 1
for i in range(1, N + 1):
  fact[i] = r = r * i % MOD
rfact[N] = r = pow(fact[N], MOD - 2, MOD)
for i in range(N, 0, -1):
  rfact[i - 1] = r = r * i % MOD


def add_length(n):
  if n < 10:
    return 2 - n
  elif n < 100:
    return 3 - n
  elif n < 1000:
    return 4 - n
  return 5 - n


def power_func(a, n):
  bi = str(format(n, "b"))  # 2進表現に
  res = 1
  for i in range(len(bi)):
    res = (res * res) % MOD
    if bi[i] == "1":
      res = (res * a) % MOD
  return res


def calc(L):
  n = len(L)
  ret = 26
  ret *= power_func(25, n - 1)
  ret *= fact[n]
  ret %= MOD
  cnt = 1
  prev = -1
  for i in L:
    if i == prev:
      cnt += 1
      continue
    ret *= rfact[cnt]
    cnt = 1
    prev = i
  return ret


def dfs(L, length, add, cur):
  if length == N:
    if add >= 0:
      return
    global ans
    ans += calc(L)
    ans %= MOD
    return
  for i in range(cur, 0, -1):
    nL = copy.copy(L)
    nL.append(i)
    dfs(nL, length + i, add + add_length(i), i)


dfs([], 0, 0, N)
print(ans)
