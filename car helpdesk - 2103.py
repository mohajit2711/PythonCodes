i = 0
while i==0:
    print("car is static")
    x = input("1. If you want car to move enter - (move)" + "\n"
    "2. If you want car to stop enter - (stop) " + "\n" + "3.If you want help enter - (help)" + "\n")
    if x == "move":
        print("car is moving")
    elif x == "stop":
        print("car has stopped")
    elif x == "help":
        print("This is a car helpdesk:")
        print(" press move to make car move and quit to make care stop in the next iteration")
    
    y = input("do you want to continue? Y/quit " "\n")
    if y == "Y":
        continue
    elif y == "quit":
        break
    


