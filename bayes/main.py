# ♣ - clubs (c)
# ♦ - diamonds (d)
# ♥ - hearts (h)
# ♠ - spades (s)

from random import randint

symbols = ["♣", "♦", "♥", "♠"]
values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] 

cards = []
for val in values:
    for symb in symbols:
        cards.append(val + symb)

# Choosing card
print("+-CHOOSE-+")
print("| 1. A♣  |")
print("| 2. K♦  |")
print("| 3. 3♥  |")
print("| 4. Q♥  |")
print("+--------+")
choice = int(input("> "))

chosed_card = 0
if choice == 1:
    chosed_card = "A♣"
elif choice == 2:
    chosed_card = "K♦"
elif choice == 3:
    chosed_card = "3♥"
elif choice == 4: 
    chosed_card = "Q♥"

# Calculate probability 
probability = str(round(1/len(cards) * 100, 2)) + "%"
print("Chance to draw " + chosed_card + " is " + probability)

input("\nPress enter to draw...")

# Drawin card
x = randint(0, len(cards))
drawed_card = cards[x]

new_prob = ""
if drawed_card[1] == "♦" or drawed_card[1] == "♥":
    print("\nDrawed card is red")
    if "♦" in chosed_card or "♥" in chosed_card:
        new_prob = str(round(((1/52) / (26/52)) * 100, 2)) + "%"
    else:
        new_prob = "0%" 
else:
    print("\nDrawed card is black")
    if "♦" in chosed_card or "♥" in chosed_card:
        new_prob = "0%" 
    else:
        new_prob = str(round(((1/52) / (26/52)) * 100, 2)) + "%"

print("New probability to draw " + chosed_card + " is " + new_prob)

input("\nPress enter to show symbol...")

print("\nDrawed card has " + drawed_card[1] + " symbol")
