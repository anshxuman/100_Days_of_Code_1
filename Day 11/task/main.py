import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


comp_cards = random.choices(cards, k=2)
user_cards = random.choices(cards, k=2)

print("Computer's Cards:", comp_cards)
print("User's Cards:", user_cards)

sum_comp = sum(comp_cards)
sum_user = sum(user_cards)

print("Sum of Computer's Cards =", sum_comp)
print("Sum of User's Cards =", sum_user)


if sum_comp == 21 and 11 in comp_cards:
    print("Blackjack occurred!")
    print("Computer Wins, You Lost!")

elif sum_user == 21 and 11 in user_cards:
    print("Blackjack occurred!")
    print("You Win, Computer Lost!")

else:

    while True:
        if sum_user > 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                sum_user = sum(user_cards)
                print("Ace adjusted to 1")
                print("New User Cards:", user_cards)
                print("New User Sum:", sum_user)
            else:
                print("You Lost!")
                exit()

        choice = input("Do you want another card? (yes/no): ").lower()

        if choice == "yes":
            user_cards.append(random.choice(cards))
            sum_user = sum(user_cards)
            print("User Cards:", user_cards)
            print("User Sum:", sum_user)
        else:
            break


    print("\nComputer's Turn")
    print("Computer Cards:", comp_cards)
    print("Computer Sum:", sum_comp)

    while sum_comp < 17:
        comp_cards.append(random.choice(cards))
        sum_comp = sum(comp_cards)
        print("Computer draws a card:", comp_cards)
        print("Computer Sum:", sum_comp)


    if sum_comp > 21:
        print("Computer Busted!")
        print("You Win!")

    elif sum_user > sum_comp:
        print("You Win!")

    elif sum_user < sum_comp:
        print("You Lost!")

    else:
        print("Draw!")