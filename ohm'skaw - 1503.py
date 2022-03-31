
#print("let us calculate Ohm's Law");
#i = int(input("Give current"));
 #r = int(input("Give resistance"));
#v = i*r;
#print("The value of voltage is:  " + str(v));


print("let us calculate Ohm's Law");

while (str ans != q):
    i = int(input("Give current"));
    r = int(input("Give resistance"));
    v = i*r;
    print("The value of voltage is:  " + str(v));
    ans = int(input("do you want to continue? y/q"))
    if ans=y:
        continue
    elif ans=q:
        break



