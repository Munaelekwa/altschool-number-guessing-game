import random

lives = 5
number = random.randint(1, 50)
while lives >= 0:
    guess = int(input("Guess a number between 1 and 50: "))
    if number != guess:
        lives -= 1
        if lives == 0:
            print("You have exhausted your lives for this session. Better luck next Time!")
            break
        if number % 2:
            if guess < number:
                print(f"Incorrect! Hint: number is odd and greater than {guess}")
            elif guess > number:
                print(f"Incorrect! Hint: number is odd and less than {guess}")

        else:
            if guess < number:
                print(f"Incorrect! Hint: number is even and greater than {guess}")
            elif guess > number:
                print(f"Incorrect! Hint: number is even and less than {guess}")
        print(f"You have {lives} lives remaining.")

    elif number == guess:
        print("You guessed the number correctly!")
        break