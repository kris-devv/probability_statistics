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

    


    print(num_of_c, num_of_d, num_of_h, num_of_s)

symbols = ["♣", "♦", "♥", "♠"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] 

cards = []

for val in values:
    for symb in symbols:
        cards.append(val + symb)

print("+----------------+")
print("| 1. Random card |")
print("+----------------+")
choose = int(input("> "))

calculate_probability()

if choose == 1:
    x = randint(0, len(cards))
    print(cards[x])
    cards.pop(x)

calculate_probability()
