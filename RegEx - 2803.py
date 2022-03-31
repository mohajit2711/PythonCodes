import re

#pattern = '^a...s$'
#test_string = 'abyss'
#result = re.match(pattern, test_string)
#if result:
 #   print("Search Succesful")
#else:
 #   print('Search unsuccesful'


# findall
#s = "the rain in spain. this is a python program"
#pattern = 'program\Z'
#result = re.findall(pattern, s)
#print(result)

#x = re.findall('ai', s)
#print(x)

# split

#text = 'the rain in spain'
#y = re.split('\s', text)
#print(y)

#pin

#pin = input('Enter pin: ')
#pattern = [1-3][4-6][7+9][0]
#x = re.match(patern, pin)
#if x:
 #   print("valid pin")
#else:
 #   print("Not Valid")

#mobile number

#num = input("Enter the mobile number: ")
#x = re.match('\d{10}\Z',num)

#if x:
   # print('valid no.')
#else:
 #   print('invalid no.')

#email id

email = input("Enter Email ID:  ")
y = re.match('\w @ \Z',  email)
if y:
    print("Valid Email.")
else:
    print("Invalid Email")