class Dist:
    def getdist(self):
        try:
            u = int(input("Enter initial velocity "))
            t = int(input("Enter average time "))
            a = int(input("Enter average acceleration "))
            s = (u * t) + 1 / 2 * (a * t * t)
            print("Distance is: ", str(s))
        except ValueError:
            print("Data type is only integer")



dist1 = Dist()
dist1.getdist()