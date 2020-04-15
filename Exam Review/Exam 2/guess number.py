import random

def main():
    GUESSES = 5


    comp_number = random.randint(1, 100)

    guess = 0
    user_number = 0

    print(comp_number)
    
    while user_number != comp_number and guess < GUESSES:
        guess += 1
        print("This is guess", guess)
        user_number = int(input("Guess a number: "))
        if user_number < comp_number:
            print("That guess was too low.")
        elif user_number > comp_number:
            print("That guess was too high.")
        else:
            print("That was the correct guess.")

    if user_number != comp_number:
        print("You ran out of guesses\n"
              "The correct number was", user_number)

main()
