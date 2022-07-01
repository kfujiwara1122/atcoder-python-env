import heapq

S = {}
ma = []
mi = []
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x = q
        if x not in S:
            heapq.heappush(ma, -x)
            heapq.heappush(mi, x)
            S[x] = 1
        else:
            S[x] += 1
    elif q[0] == 2:
        _, x, c = q
        if x in S:
            if S[x] - c > 0:
                S[x] = S[x] - c
            else:
                S.pop(x)
    elif q[0] == 3:
        maxval, minval = -1, -1
        # print(ma, mi, S)
        while True:
            tmp = heapq.heappop(ma)
            if -tmp in S:
                maxval = -tmp
                heapq.heappush(ma, tmp)
                break
        while True:
            tmp = heapq.heappop(mi)
            if tmp in S:
                minval = tmp
                heapq.heappush(mi, tmp)
                break
        print(maxval - minval)
