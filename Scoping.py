x = 0

def outer():
    x = 1
    print(x)
    def inner():
        x = 2
        print(x)
    inner()
outer()
inner()
