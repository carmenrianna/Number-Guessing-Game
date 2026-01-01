import random

print("\nHello, I'm Sae. This is my 2nd time making a program using Python.")
print("\n--- NUMBER GUESSING GAME ---")

random_num = random.randint(1, 100)
print(random_num)

print("I am thinking of a number between 1 and 100.")

isTrue = True

while isTrue:
    guess = int(input("Take a guess: "))

    if guess == random_num:
        print("\nYou guessed it!")
        isTrue = False
    else:
        distance = abs(random_num - guess)

        if distance > 50:
            print("You're too far!")
        elif 25 < distance <= 50:
            print("You're close!")
        elif 10 < distance <= 25:
            print("You're so much closer!")
        elif 5 < distance <= 10:
            print("Almost there!")
        else:
            print("You're extremely close!")
