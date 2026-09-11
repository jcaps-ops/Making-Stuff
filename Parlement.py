import random

#State name,[votes],population,votertype
states = [["State1",[],120,"Standerd"],["State2",[],150],["Capital",[],2000],["Ruralstate1",[],50],["Urbanstate",[]],50]

def parlement(states):
    num1seats = 0
    num2seats = 0
    num1votetypes = []
    num2votetypes = []
    for x in states:
        if x[1] == []:
            n1rand = random.randrange(0,x[2])
            n2rand = x[2] - n1rand
            #n2rand = random.randrange(0,100)
            x[1].append(n1rand)
            x[1].append(n2rand)
            print(f"{x[0]}: 1:{x[1][0]} 2:{x[1][1]}")
            if x[1][0] > x[1][1]:
                num1seats += 4
            elif x[1][0] < x[1][1]:
                num2seats += 4
            else:
                print(f"{x[0]} resulted in a tie")
    print(f"Party 1 got {num1seats} in parlement")
    print(f"Party 2 got {num2seats} in parlement")

parlement(states)