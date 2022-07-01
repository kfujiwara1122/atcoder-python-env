H, W = list(map(int, input().split()))
X, Y = [], []
S = []
for h in range(H):
    s = input()
    for w in range(W):
        if s[w] == "o":
            X.append(h)
            Y.append(w)
# print(X, Y)
print(abs(X[0] - X[1]) + abs(Y[0] - Y[1]))
