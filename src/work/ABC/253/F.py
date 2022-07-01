N, M, Q = list(map(int, input().split()))
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, l, r, x = q
        S[x] += 1
    elif q[0] == 2:
        _, x, c = q
        S[x] -= c
        if S[x] <= 0:
            S.pop(x)
    elif q[0] == 3:
        tmp = S.keys()
        tmp = sorted(tmp)
        print(abs(tmp[0] - tmp[-1]))
