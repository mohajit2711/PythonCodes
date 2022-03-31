# make two lists - keys and values and convert into dictionary

# a = ('1', '2', '3', '4', '5')
# b = ('abc', 'xyz', 'lmn', 'pqr', 'stu')
#
# dict1 = dict(zip(a,b))
# print(dict1)
# print(type(dict1))

# create a dictionary and extract some required keys from it

x = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e'}
print("dictionary: ", x)

y = ('2', '3', '6')
for i in range(len(y)):
    if y[i] in x.keys():
        print(y[i], ": ", x.get(y[i]))
    else:
        print('requested key not present in dictionary: ', y[i])