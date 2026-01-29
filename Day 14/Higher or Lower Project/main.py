import art
import random
import game_data

print(art.logo)

score = 0
game_on = True

person1 = random.choice(game_data.data)
person2 = random.choice(game_data.data)

while game_on:

    if person1 == person2:
        person2 = random.choice(game_data.data)

    print(f"Compare A : {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(art.vs)
    print(f"Against B : {person2['name']}, a {person2['description']}, from {person2['country']}.")

    inp = input("Who has more followers?\nType 'A' or 'B' : ").lower()

    a_followers = person1["follower_count"]
    b_followers = person2["follower_count"]

    print("\n" * 20)
    print(art.logo)

    if (inp == "a" and a_followers > b_followers) or (inp == "b" and b_followers > a_followers):
        score += 1
        print(f"You're right! Current score: {score}")
        person1 = person2
        person2 = random.choice(game_data.data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False