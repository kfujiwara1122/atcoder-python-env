import heapq


N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append((b, c, i + 1))
    G[b].append((a, c, i + 1))
Q = [(0, 0, -1)]
visited = [False] * N
while Q:
    c, at, prev = heapq.heappop(Q)
    if visited[at]:
        continue
    visited[at] = True
    if prev > 0:
        print(prev, end=" ")
    for tmp, tc, m in G[at]:
        if not visited[tmp]:
            heapq.heappush(Q, (c + tc, tmp, m))
