import random
number = random.randint(1, 100)
print("Guess the number between 1 and 100, You have 3 chances")
for i in range(3):
    guess = int(input(f"Attempt {i + 1}: Enter your guess: "))

    if guess == number:
        print("You guessed it!")
        break
    elif guess < number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

else:
    print(f"Out of chances, The correct number was {number}.")
