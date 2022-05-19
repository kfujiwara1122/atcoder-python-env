N = 100
A = [[]]
for _ in range(N):
  # print('input')
  a = list(map(int, input().split()))
  A.append(a)
for n in range(2, N + 1):
  print(f"start process n = {n}")
  for i in range(n):
    if i == 0:
      A[n][i] = A[n][i] + A[n - 1][i]
    elif i == n - 1:
      A[n][i] = A[n][i] + A[n - 1][i - 1]
    else:
      A[n][i] = A[n][i] + max(A[n - 1][i - 1], A[n - 1][i])
print(max(A[N]))
