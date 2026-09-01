import random

deck = ["1","2","3","4","5","6","7","8","9","10"]
Dealers_Deck = ["1","2","3","4","5","6","7","8","9","10"]
Boons = []
potentialboons = []
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
def store():
    pass
        
        
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