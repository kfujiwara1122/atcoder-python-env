N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sA = set()
sB = set()

same = []

iB = 0
for iA, a in enumerate(A):
  sA.add(a)
  tmp1 = -1
  tmp2 = -1
  while iB < N and len(sA) > len(sB):
    sB.add(B[iB])
    iB += 1
  tmp1 = iB - 1
  while iB < N and B[iB] in sB:
    sB.add(B[iB])
    iB += 1
  tmp2 = iB - 1
  if sA == sB:
    same.append((tmp1, tmp2))
  else:
    same.append((-1, -1))
# print(same)
Q = int(input())
for _ in range(Q):
  x, y = list(map(int, input().split()))
  x -= 1
  y -= 1
  if same[x][0] <= y <= same[x][1]:
    print('Yes')
  else:
    print('No')
