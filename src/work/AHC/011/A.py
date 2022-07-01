N, T = map(int, input().split())
t = []
i0, j0 = -1, -1
for i in range(N):
  s = input()
  tmp = []
  for c, j in enumerate(s):
    n = int(c, 16)
    tmp.append(n)
    if n == 0:
      i0 = i
      j0 = j
  t.append(tmp)


def move(
        board: list(list(int)),
        score: int,
        direction: str
) -> int:
  pass
