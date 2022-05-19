# 典型90-12
# https://atcoder.jp/contests/typical90/tasks/typical90_l

class UnionFindTree:
  def __init__(self, size=10 ** 6):
    assert size > 0


H, W = map(int, input().split())
S = []
for _ in range(H):
  S.append(input())
