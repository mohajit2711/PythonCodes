#exception handling - a condition where at runtime execution gets interrupted
import builtins
i = 0
x = ' '
while i==0:
    try:
        age = int(input("Enter your age: "))
        print(age)
    except ValueError:
        print("Wrong data type")
        x = input("Run program again? Y/N: ")
        if x=='Y':
            continue
        else:
            break
print("Program is over.")