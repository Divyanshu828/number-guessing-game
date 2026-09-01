import random

print("🎯 Welcome to the Number Guessing Game!")

best_score = None

while True:

    number = random.randint(1, 100)
    i = 0

    while True:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if 0 < guess <= 100:

            i += 1

            if guess < number:
                print("Guess higher")

            elif guess > number:
                print("Guess lower")

            else:
                print(f"You got it in {i} guesses!")

                if best_score is None or i < best_score:
                    best_score = i
                    print("Congrates🎉 Your New best score!")

                print(f"Best score: {best_score} guesses")

                break

            # Give a hint after 3 wrong guesses
            if i == 3:
                if number > 50:
                    print("💡 Hint: The number is greater than 50.")
                else:
                    print("💡 Hint: The number is 50 or less.")

        else:
            print("Error: Please give a number between 1 and 100")

    again = input("Play again? (y/n): ")

    if again.lower() != "y":
        print(f"Your best score was {best_score} guesses.")
        break