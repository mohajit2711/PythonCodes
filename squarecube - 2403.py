a = [1,4,9,16,25,36,49,64,81,100]
b = [1,8,27,64,125,216,343,512,729,1000]
c = []
for m in range(len(a)):
    if a[m]%2 == 0:
        c.append((a[m]))

for n in range(len(b)):
    if b[n]%2 == 0:
        c.append((b[n]))
c.sort()
print(c)

