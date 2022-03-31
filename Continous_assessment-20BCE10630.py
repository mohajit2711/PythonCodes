#Mohajit Paul 20BCE10630
#Python Programming Continous Assessment
# Write a program to print the sum of the following series 1 + 1/2 + 1/3 +. …. + 1/n
n = int(input("Enter the limit of the series: "))
i = 1
for i in range(1,n):
    i = 1 / i
    sum = i + 1
    i+=1
    print(sum)

#Write Python program to perform a linear search for a given Key number in the list and report Success or Failure.

a = (1,2,3,4,5,6,7,8,9,10)
i = 0
while i == 0:
    n = int(input("Enter the desired key: "))
    if n in a:
        print("Success")
    else:
        print("Failure")

    x = input("Do you want to continue? Y/N ")
    if x == 'Y':
        continue
    elif x == 'N':
        break

#Write a Python Program to input information for n number of students as given below: (Use OOP concepts)

class Student:
    def student1(self):
        i = 0
        while i == 0:
            name = input("Enter the name for student: ")
            regno = input("Enter the student's roll number: ")
            totmark = input("Enter the total marks for student: ")

            a = {name: (regno, totmark)}
            print(a)
            x = input("Do you want to continue? Y/N ")
            if x == 'Y':
                continue
            elif x == 'N':
                break

stud1 = Student()
stud1.student1()