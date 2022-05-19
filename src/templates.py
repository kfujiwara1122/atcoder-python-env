# imports
import bisect
import heapq
from collections import defaultdict
from collections import deque
from string import ascii_lowercase as lc

# map input
a, b, c = list(map(int, input().split()))

# list input
N = int(input())
A = list(map(int, input().split()))

# 2D grid input
H, W = list(map(int, input().split()))
S = []
for _ in range(H):
  s = input()
  S.append(s)

# graph input
N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
  a, b = list(map(int, input().split()))
  a -= 1
  b -= 1
  G[a].append(b)
  G[b].append(a)
