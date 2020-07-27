import random

print("------------------------------")
print("       M&M Guessing Game      ")
print("------------------------------")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print("Guess the number of M&Ms and you get lunch on the house!")
print()

while attempts < attempt_limit:
    attempts += 1
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)

    if mm_count == guess:
        print(f"You win, baby! It was {guess}.")
        break
    elif guess < mm_count:
        print("Sorry! That's too low")
    else:
        print("That's too High!")

print(f"Bye, you finished in {attempts} attempt.")
