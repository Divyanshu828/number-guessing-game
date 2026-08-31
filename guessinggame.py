import random

print("Start small. Ship something.")

best_score = None

while True:

    number = random.randint(1, 100)
    i = 0

    while True:

        guess = int(input("Enter your guess: "))

        if 0 < guess <= 100:

            i += 1

            if guess < number:
                print("Guess higher")

            elif guess > number:
                print("Guess lower")

            else:
                print(f"You got it in {i} guesses!")

                # Best score tracker
                if best_score is None or i < best_score:
                    best_score = i
                    print("🎉 New best score!")

                print(f"Best score: {best_score} guesses")

                break

        else:
            print("Error: Please give number between 1 and 100")

    again = input("Play again? (y/n): ")

    if again.lower() != "y":
        print(f"Your best score was {best_score} guesses.")
        break