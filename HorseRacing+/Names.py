import random



def NameGen():
    N = ["Green","dream","hope","blue","night","sky","dawn","red","purple","fall","Gentle","Speedy"]
    RN1 = N[random.randrange(0,len(N))]
    checking = True
    while checking:
        RN2 = N[random.randrange(0,len(N))]
        if RN2 == RN1:
            pass
        else:
            checking = False
    RN = str(RN1 + " " + RN2)
    return RN

Name = NameGen()
print(Name)

