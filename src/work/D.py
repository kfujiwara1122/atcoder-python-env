N = int(input())
A = list(map(int, input().split()))
C = [0] * (2 * 10 ** 5 + 1)

for a in A:
  C[a] += 1
ans = 0
for j in range(1, 10 ** 5 + 1):
  i = j
  while i <= 10 ** 5:
    k = i // j
    ans += C[i] * C[j] * C[k]
    i += j
print(ans)
