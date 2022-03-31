sample = {'one': 1 , 'two': 2, 'three':3, 'four':4, 'five': 5}
print (sample)
k = []
i = 0
while i ==0:
    x = input("Enter the key for dictionary: ")
    k.append(x[i])
    ans = "Do you want to print more? Y/N"
    if x == 'Y':
        continue
    else:
        break
print(k)