import heapq

N, K = list(map(int, input().split()))
M = N - K  # 採用クエリの最小数
Q = []
for _ in range(N):
  t, y = list(map(int, input().split()))
  Q.append((t, y))
Q = reversed(Q)
dp = [0] * (M + 1)
add = heapq([])

ans = 0
for (t, y), i in enumerate(Q):
  if t == 1:
