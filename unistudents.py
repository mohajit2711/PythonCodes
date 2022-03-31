uni1 = (["a","b","c","d","e"])
uni2 = (["f","g","h","i","j"])
uni3 = ([])
uni3 = uni2
x = str(input("does a want to change his subject? Y/N"))
def stMove(stNum, subTo):
    subTo.append(stNum)
    print(subTo)
stMove(uni1[0], uni2)