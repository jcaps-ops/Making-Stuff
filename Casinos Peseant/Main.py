import random

deck = ["1","2","3","4","5","6","7","8","9","10"]
Dealers_Deck = ["1","2","3","4","5","6","7","8","9","10"]
Boons = []
potentialboons = ["Chip mult","Token+","Slasher","Coming Death","Daily double"]
pot_deck = ["-3","Joker","Cashback","Death","Twins"]
SinkHole = 75
total = 0
dealer_total = 0
Cash = 50
Chip = 0
Chipmult = 3
def calculate(Deck,Total):
    card = Deck[random.randrange(0,len(Deck))]
    try:
        Total += int(card)
    except:
        pass
    return Total,card
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
        print(f"You drew Death it cut your qouta by 1/4th")
        print(f"Your qouta before the cut was {Quota}")
        Quota = Quota * 3
        Quota = Quota / 4
        Quota = round(Quota)
        print(f"Your current quote is {Quota}")
    return deck,Cash,Chip,Quota
def boonInteraction(boons,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole):
    
    if "Token+" in boons:
        Chip += 1
        print("Token plus gave you plus 1 token")
    if "Slasher" in boons:
        while True:
            ply_inp = input("Please put in what card to delete")
            try:
                deck.remove(ply_inp)
                break
            except:
                print("That is not a card in your deck")
        while True:
            ply_inp = input("Please put in what number card to add")
            try:
                plyint = plyint(ply_inp)
                if ply_inp > 0:
                    str(ply_inp)
                    deck.append(ply_inp)
                    break
                else:
                    print("Your card can not be a negative")
            except:
                print("That a acceptable card")
    if "Coming Death" in boons:
        Quota *= 1.25
        Quota = round(Quota)
        pc = Chip
        Chip *= 1.5
        Chip = round(Chip)
        print(f"Coming death has activated making your qouta {Quota} but gave you {Chip-pc}")
    if "Daily double" in boons:
        rand = random.randrange(1,10)
        if rand == 1:
            pc = Cash
            Cash = Cash * 2
            print(f"Your daily double kicked in earning you {Cash - pc}")
    return boons,deck,Cash,Chip,Quota
def blackjack(deck=deck,total=total,Cash=Cash,Dealerdeck = Dealers_Deck,dealer_total = dealer_total,SinkHole=SinkHole,Chip = Chip,boons=Boons):
    print(f"The current quote you have to reach is {SinkHole}$.")
    for x in range(0,3):
        if Cash == 0 or Cash < 0:
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
            total = int(total)
            deck,Cash,Chip,SinkHole = cardeffectcalc(card,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole)
            total,card = calculate(deck,total)
            total = int(total)
            deck,Cash,Chip,SinkHole = cardeffectcalc(card,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole)
            print(f"Your total is {total}")
            while True:
                action = input("Stand or Hit:")
                if action == "Stand" or action == "stand":
                    break
                if action == "Hit" or action == "hit":
                    total,card = calculate(deck,total)
                    deck,Cash,Chip,SinkHole = cardeffectcalc(card,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole)
                    print(total)
                    if total > 21:
                        print("You Busted")
                        total = 0
                        break
            while True:
                if dealer_total < 18:
                    dealer_total,Dealer_card = calculate(Dealerdeck,dealer_total)
                    if dealer_total > 21:
                        dealer_total = 0
                        break
                else:
                    break
            print(f"Dealers total is {dealer_total}")
            print(f"Your bet was {bet}")
            print(Cash)
            if dealer_total > total:
                print("Dealers win")
                Cash -= bet
            elif dealer_total < total:
                print("You win")
                Cash += bet
            else:
                print("You Tied")
                pass
            boons,deck,Cash,Chip,SinkHole = boonInteraction(boons,deck=deck,Cash=Cash,Chip=Chip,Quota=SinkHole)
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
        random_num = random.randrange(1,3)
        if random_num == 1:
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
                elif z in pot_deck:
                    Chip -= zpr
                    deck.append(z)
                    pot_deck.remove(z)
                else:
                    print("What how did you do this")
            else:
                print("You can not afford this")
    if "chip mult" in boons:
        Chipmult += 2
        boons.remove("chip mult")

    
    print()
def figurePrice(Item):
    if Item == "Chip mult":
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
    elif Item == "Coming Death":
        price = 1

    return price
        

while True:
    deck,total,Cash,Chip,SinkHole = blackjack(deck,total,Cash,Dealers_Deck,dealer_total,SinkHole)
    if Cash == 0:
        break
    if Cash < SinkHole:
        break
    Chip += DealChip(Cash)
    print(f"You currently have {Chip} Chips.")
    store(Chip)
    print(f"This is your deck {deck} \n This are your boons {Boons}")
    SinkHole = SinkHole * 1.5
    SinkHole = round(SinkHole)
print("YOU LOSE")