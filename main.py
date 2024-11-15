# ♣ - clubs (c)
# ♦ - diamonds (d)
# ♥ - hearts (h)
# ♠ - spades (s)

from random import randint

def calculate_probability():
    num_of_all_cards = len(cards)

    num_of_symbols = [] # [n♣, n♦, n♥, n♠]
    for symb in symbols:
        num_of_symbols.append(len([x for x in cards if symb in x]))

    perc_for_symbols = [] # [♣%, ♦%, ♥%, ♠%]
    for num in num_of_symbols:
        perc_for_symbols.append(str(round(num / num_of_all_cards * 100, 2)) + "%")

    for i, symb in enumerate(symbols):
        print("Chance for " + symb + " : " + perc_for_symbols[i])
    
symbols = ["♣", "♦", "♥", "♠"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] 

cards = []
for val in values:
    for symb in symbols:
        cards.append(val + symb)

calculate_probability()

run = True
while(run):
    print("+----------------+")
    print("| 1. Random card |")
    print("| 0. Exit        |")
    print("+----------------+")
    choose = int(input("> "))

    if choose == 1:
        x = randint(0, len(cards)-1)
        print(cards[x])
        cards.pop(x)
    elif choose == 0:
        run = False
        continue

    calculate_probability()
