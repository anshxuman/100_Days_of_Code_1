import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy version
al = ""
for a in range(0,nr_letters):
    al = al + random.choice(letters)
for b in range(0,nr_symbols):
    al = al + random.choice(symbols)
for c in range(0,nr_numbers):
    al = al + random.choice(numbers)
print(f"IF YOU ANT THE PASSWORD IN SEQUENCE: {al}")

#hard version
a1 = []
for d in range(0,nr_letters):
    a1.append(random.choice(letters))
for e in range(0,nr_symbols):
    a1.append(random.choice(symbols))
for f in range(0,nr_numbers):
    a1.append(random.choice(numbers))
random.shuffle(a1)
a2 = ""
a3 = a2.join(a1)
print(f"IF YOU ANT THE PASSWORD IN RANDOM SEQUENCE: {a3}")
