import random
a = []
b = []
for i in range(100):
    if i%3==0:
        a.append(i)
    else:
        pass
for j in range(100):
    if j%5==0:
        b.append(j)
    else:
        pass
print(a)
print(b)
print(list(set(a).intersection(list(set(b)))))

