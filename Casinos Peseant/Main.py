import random

deck = ["1","2","3","4","5","6","7","8","9","10"]
Dealers_Deck = ["1","2","3","4","5","6","7","8","9","10"]
Boons = []
potentialboons = ["Chip mult","Token+"]
pot_deck = ["-3","Joker","Cashback","Death","Twins"]
SinkHole = 75
total = 0
dealer_total = 0
Cash = 50
Chip = 0
Chipmult = 3
def roll(deck):
    card = deck[random.randrange(0,len(deck))]
    return card
def calculate(deck,total):
    card = roll(deck)
    print(card)
    try:
        total += int(card)
        print("tried")
    except:
        pass
    return total,card
def cardeffectcalc(card,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole):
    if card == "Cashback":
            Cash += 20
            print("You drew your Cash back card")
    elif card == "Twins":
            card1 = deck[random.randrange(0,len(deck))]
            deck.append(card1)
            print(f"You drew the twins card it duplicated the {card1}")
    elif card == "Joker":
            jokervaluechip = random.randrange(-5,10)
            JVC = random.randrange(-10,75)
            Chip += jokervaluechip
            Cash += JVC
            print(f"You drew the Joker card it gave you {jokervaluechip} Chip and {JVC} Cash")
    elif card == "Death":
            Quota = Quota / 2
            print(f"You drew Death it cut your qouta in half")
            print(f"Your current quote is {Quota}")
    return deck,total,Cash,Chip,SinkHole
    
def blackjack(deck=deck,total=total,Cash=Cash,Dealerdeck = Dealers_Deck,dealer_total = dealer_total,SinkHole=SinkHole,Chip = Chip):
    print(f"The current quote you have to reach is {SinkHole}$.")
    for x in range(0,3):
        if Cash == 0:
            pass
        else:
            total = 0
            dealer_total = 0
            print("New game")
            print(f"You currently have {Cash}$")
            while True:
                bet_input = input("Please put in bet:")
                try:
                    bet = int(bet_input)
                    if bet <= Cash:
                        break
                    else:
                        print("You put a bet greater than the amount of Cash you have")
                except:
                    print("That is not an Accepted number")
            total,card = calculate(deck,total)
            deck,total,Cash,Chip,SinkHole = cardeffectcalc(card)
            total,card = calculate(deck,total)
            deck,total,Cash,Chip,SinkHole = cardeffectcalc(card)
            print(f"Your total is {total}")
            while True:
                action = input("Stand or Hit:")
                if action == "Stand" or action == "stand":
                    break
                if action == "Hit" or action == "hit":
                    total,card = calculate(deck,total)
                    deck,total,Cash,Chip,SinkHole = cardeffectcalc(card)
                    print(total)
                    if total > 21:
                        print("You Busted")
                        total = 0
                        break
            while True:
                if dealer_total < 18:
                    dealer_total= calculate(Dealers_Deck,dealer_total)
                    if dealer_total > 21:
                        dealer_total = 0
                        break
                else:
                    break
            print(f"Dealers total is {dealer_total}")
            print(f"Your bet was {bet}")
            if dealer_total > total:
                print("Dealers win")
                Cash -= bet
            elif dealer_total < total:
                print("You win")
                Cash += bet
            else:
                print("You Tied")
                pass
    return deck,total,Cash,Chip,SinkHole
        
            
def DealChip(Cash,Chip=Chip,Chipmult = Chipmult,sinkhole = SinkHole):
    chipqouta = Cash/sinkhole
    print(f"This is your Cash {Cash}")
    print(f"This is your chips before multipler {chipqouta}")
    Chip += round(Chipmult * chipqouta)
    print(Chip)
    return Chip
def store(Chip,boons=Boons,pot_boon=potentialboons,deck=deck,pot_deck=pot_deck):
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
    print("Here are you options if you do not want to buy something type exit.")
    print(f"1-{x} for {xpr} Chip\n2-{y} for {ypr} Chip \n3-{z} for {zpr} Chip")
    while True:
        ply_inp = input("")
        if ply_inp == "Exit" or ply_inp == "exit" or ply_inp == "e" or ply_inp == "E":
            break
        if ply_inp == "1" or ply_inp == x:
            if xpr <= Chip:
                if x in pot_boon:
                    Chip -= xpr
                    boons.append(x)
                    pot_boon.remove(x)
                elif x in pot_deck:
                    Chip -= xpr
                    deck.append(x)
                    pot_deck.remove(x)
                else:
                    print("What how did you do this")
            else:
                print("You can not afford this")
                print(f"You currently have only {Chip} and it costs {xpr}")
        elif ply_inp == "2" or ply_inp == y:
            if ypr <= Chip:
                if y in pot_boon:
                    Chip -= ypr
                    boons.append(y)
                    pot_boon.remove(y)
                elif y in pot_deck:
                    Chip -= ypr
                    deck.append(y)
                    pot_deck.remove(y)
                else:
                    print("What how did you do this")
            else:
                print("You can not afford this")
                print(f"You currently have only {Chip} and it costs {ypr}")
        elif ply_inp == "3" or ply_inp == z:
            if zpr <= Chip:
                if z in pot_boon:
                    Chip -= zpr
                    boons.append(z)
                    pot_boon.remove(z)
                elif x in pot_deck:
                    Chip -= zpr
                    deck.append(z)
                    pot_deck.remove(z)
                else:
                    print("What how did you do this")
                    print(f"You currently have only {Chip} and it costs {zpr}")
            else:
                print("You can not afford this")

    
    print()
def figurePrice(Item):
    if Item == "Chip,mult":
        price = 5
    elif Item == "Token+":
        price = 3
    elif Item == "Cash+":
            price = 3
    elif Item == "Daily double+":
        price = 3
    elif Item == "-3":
        price = 2
    elif Item == "Joker":
        price = 1
    elif Item == "Cashback":
        price = 5
    elif Item == "Death":
            price = 7
    elif Item == "Twins":
            price = 10

    return price
        

while True:
    deck,total,Cash,Chip,SinkHole = blackjack(deck,total,Cash,Dealers_Deck,dealer_total,SinkHole)
    if Cash == 0:
        break
    if Cash < SinkHole:
        break
    Chip = DealChip(Cash)
    print(f"You currently have {Chip} Chips.")
    store(Chip)
    print(f"This is your deck {deck} \n This are your boons {Boons}")
    SinkHole = SinkHole * 1.5
    SinkHole = round(SinkHole)
print("YOU LOSE")