Number = int(input("\n Enter the Range : "))
i = 0
a = 0
b = 1

while(i < Number):
    if(i <= 1):
        Next = i
    else:
        Next = a + b
        a = b
        b = Next
    print(Next)
    i = i + 1