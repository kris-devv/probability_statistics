from random import randint

# ♣ - clubs (c)
# ♦ - diamonds (d)
# ♥ - hearts (h)
# ♠ - spades (s)

def calculate_probability():
    num_of_c = len([c for c in cards if "♣" in c])
    num_of_d = len([d for d in cards if "♦" in d])
    num_of_h = len([h for h in cards if "♥" in h])
    num_of_s = len([s for s in cards if "♠" in s])
    num_of_all_cards = len(cards)

    perc_c = str(round(num_of_c / num_of_all_cards * 100, 2)) + "%"
    perc_d = str(round(num_of_d / num_of_all_cards * 100, 2)) + "%"
    perc_h = str(round(num_of_h / num_of_all_cards * 100, 2)) + "%"
    perc_s = str(round(num_of_s / num_of_all_cards * 100, 2)) + "%"
    
    print("Chance for ♣ : " + perc_c)
    print("Chance for ♦ : " + perc_d)
    print("Chance for ♥ : " + perc_h)
    print("Chance for ♠ : " + perc_s)
    

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
