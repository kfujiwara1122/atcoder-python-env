ans = 0
for i in range(100, 1000):
  for j in range(i, 1000):
    t = i * j
    ts = str(t)
    if ts == ts[::-1]:
      ans = max(ans, t)
print(ans)
