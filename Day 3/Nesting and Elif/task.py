print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter the age of the person supposed to ride: "))
    if age > 18:
        print("The ticket price is $12")
    else:
        print("The ticket price is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
