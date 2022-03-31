a = [1,2,3,4,5]
#list a
b = [2,8,3,4,5]
#list b
a.append(3)
#list appended with 3
print(a)
a.extend(b)
#list extended putting all elements of b in a
print(a)
a.insert(2,10)
#list inserts 10 at position 2
print(a)
a.sort()
#list gets sorted
print (a)
a.reverse()
#list is reversed
print (a)
a.reverse()
#list is reversed
print (a)
print(a.index(2))
#list gives index of number given in arguement
print(a.pop())
