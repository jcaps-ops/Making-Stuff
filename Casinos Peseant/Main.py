import random

deck = ["1","2","3","4","5","6","7","8","9","10"]
Dealers_Deck = ["1","2","3","4","5","6","7","8","9","10"]
Boons = []
potentialboons = ["Chip mult","Token+"]
pot_deck = ["-3","Jocker","Cashback"]
SinkHole = 75
total = 0
dealer_total = 0
Cash = 50
Chip = 0
Chipmult = 5
def roll(deck):
    card = deck[random.randrange(0,len(deck))]
    return card
def calculate(deck,total):
    card = roll(deck)
    try:
        total += int(card)
    except:
        print("It Failed")
    return total
    
def blackjack(deck=deck,total=total,cash=Cash,Dealerdeck = Dealers_Deck,dealer_total = dealer_total,SinkHole=SinkHole):
    print(f"The current quote you have to reach is {SinkHole}$.")
    for x in range(0,3):
        if cash == 0:
            pass
        else:
            total = 0
            dealer_total = 0
            print("New game")
            print(f"You currently have {cash}$")
            while True:
                bet_input = input("Please put in bet:")
                try:
                    bet = int(bet_input)
                    if bet <= cash:
                        break
                    else:
                        print("You put a bet greater than the amount of cash you have")
                except:
                    print("That is not an Accepted number")
            total = calculate(deck,total)
            total = calculate(deck,total)
            print(f"Your total is {total}")
            while True:
                action = input("Stand or Hit:")
                if action == "Stand" or action == "stand":
                    break
                if action == "Hit" or action == "hit":
                    total = calculate(deck,total)
                    print(total)
                    if total > 21:
                        print("You Busted")
                        total = 0
                        break
            while True:
                if dealer_total < 18:
                    dealer_total = calculate(Dealers_Deck,dealer_total)
                    if dealer_total > 21:
                        dealer_total = 0
                        break
                else:
                    break
            print(f"Dealers total is {dealer_total}")
            if dealer_total > total:
                print("Dealers win")
                cash -= bet
            elif dealer_total < total:
                print("You win")
                cash += bet
            else:
                print("You Tied")
                pass
    return cash
        
            
def Dealchips(Chips=Chip,Cash=Cash,Chipmult = Chipmult,sinkhole = SinkHole):
    Chips = round(Chipmult * (Cash/sinkhole))
    return Chips
def store(chip=Chip,boons=Boons,pot_boon=potentialboons,deck=deck,pot_deck=pot_deck):
    storeop = []
    for x in range (0,3):
        if random.randrange(1,2) == 1:
            storeop.append(pot_deck[random.randrange(0,len(pot_deck))])
        else:
            storeop.append(pot_boon[random.randrange(0,len(pot_boon))])
    x = storeop[0]
    xpr = figurePrice(x)
    y = storeop[1]
    ypr = figurePrice(y)
    z = storeop[2]
    zpr= figurePrice(z)
    print("Here are you options if you do not want to buy 1 type exit.")
    print(f"1-{x} for {xpr} chips\n2-{y} for {ypr} chips \n 3-{z} for {zpr} chips")
    while True:
        ply_inp = input("")
        if ply_inp == "1":
            pass

    
    print()
def figurePrice(Item):
    if Item == "Chip,mult":
        price = 5
    elif Item == "Token+":
        price = 3
    elif Item == "cash+":
            price = 3
    elif Item == "Daily double+":
        price = 3
    elif Item == "-3":
        price = 2
    elif Item == "Jocker":
        price = 1
    elif Item == "Cashback":
        price = 5

    return price
        

potentialboons = ["Chip mult","Token+","cash+","Daily Double"]
pot_deck = ["-3","Jocker","Cashback"]

while True:
    Cash = blackjack(deck,total,Cash,Dealers_Deck,dealer_total,SinkHole)
    if Cash == 0:
        break
    if Cash < SinkHole:
        break
    chips = Dealchips()
    print(f"You currently have {chips} chips.")
    SinkHole = SinkHole * 1.5
    SinkHole = round(SinkHole)
print("YOU LOSE")