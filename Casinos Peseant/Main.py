import random

deck = ["1","2","3","4","5","6","7","8","9","10"]
Dealers_Deck = ["1","2","3","4","5","6","7","8","9","10"]
total = 0
dealer_total = 0
Cash = 50
Chip = 0
def roll(deck):
    card = deck[random.randrange(0,len(deck))]
    print(f"card is {card}")
    return card
def calculate(deck,total):
    card = roll(deck)
    try:
        print("test")
        total += int(card)
    except:
        print("It Failed")
    return total
    
def blackjack(deck=deck,total=total,cash=Cash,Dealerdeck = Dealers_Deck,dealer_total = dealer_total):
    for x in range(0,3):
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
        total += calculate(deck,total)
        total += calculate(deck,total)
        print(f"Your total is {total}")
        while True:
            action = input("Pass or Hit:")
            if action == "Pass":
                break
            if action == "Hit":
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
        
        
        

blackjack(deck,total)