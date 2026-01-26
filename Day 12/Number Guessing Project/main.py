import random

print("welcome to the number guessing game!")
print("I'm Thinking of a number between 1 and 100")
diff=input("Choose your difficulty level : 'Easy' OR 'HARD' : ").lower()
number = random.randint(1,100)
#print(number)

if diff == "easy":
    attempts = 10
    for i in range(1,11):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = attempts - 1

        if guess == number:
            print("Nice Guess, You got it right!")
            break

        elif guess > number:
            print("Number Too Big")
            print("Guess Again")
            continue

        elif guess < number:
            print("Number Too Small")
            print("Guess Again")
            continue

    else:
        print("Sorry, You didn't guess it right.")


if diff == "hard":
    attempts = 5
    for i in range(1, 6):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = attempts - 1

        if guess == number:
            print("Nice Guess, You got it right!")
            break

        elif guess > number:
            print("Number Too Big")
            print("Guess Again")
            continue

        elif guess < number:
            print("Number Too Small")
            print("Guess Again")
            continue
    else:
        print("Sorry, You didn't guess it right.")