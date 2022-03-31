# question 1
#a = [1,2,3]
#b  = [3,1,4]

#print("list 1 is: ", a)
#print("list 1 is: ", b)
#i=0
#for i in range(len(a)):
  #  for j in range(len(b)):
 #       if a[i] != b[j]:
#            print(" (", a[i] , "," , b[j] , " )")


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!= y:
            combs.append((x,y))
print(combs)


