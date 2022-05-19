a1 = 0
a2 = 0
for i in range(101):
  a1 += i ** 2
  a2 += i
a2 **= 2
print(a2 - a1)
