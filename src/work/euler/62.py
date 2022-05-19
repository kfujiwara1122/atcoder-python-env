from collections import defaultdict

d = defaultdict(list)
i = 0
while True:
  i += 1
  tmp = str(i ** 3)
  dt = defaultdict(int)
  for j in tmp:
    dt[j] += 1
  param = []
  for j in range(10):
    param.append(str(j))
    param.append(str(dt[str(j)]))
  key = ".".join(param)
  d[key].append(i)
  if len(d[key]) == 5:
    print(d[key][0] ** 3)
    exit()
print(d)
