import math


N, A, B = list(map(int, input().split()))


def calc(x):
    cnt = N // x
    return (x + x * cnt) * cnt // 2


sn = (N + 1) * N // 2
lcm = A * B // math.gcd(A, B)
print(sn - calc(A) - calc(B) + calc(lcm))
