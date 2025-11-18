print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        pay = 5
        print(f"TICKET PRICE : ${pay}")
    elif age <= 18:
        pay = 7
        print(f"TICKET PRICE : ${pay}")
    else:
        pay = 12
        print(f"TICKET PRICE : ${pay}")
    inp = input("Do you want photos ( yes / no ) ? : ")
    if inp == "yes":
        pay = pay + 3
        print(f"The total bill is ${pay}")
    else:
        print(f"The total bill is ${pay}")

else:
    print("Sorry you have to grow taller before you can ride.")
