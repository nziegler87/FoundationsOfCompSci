import time

BONUS_ROUND_TIME = 20

def main():
    print("You have", BONUS_ROUND_TIME, "seconds to enter "
          "your guess...starting now.")
    start_time = time.time()
    guess = input("Enter your guess: ")
    end_time = time.time()
    total_time = end_time - start_time

    if total_time <= BONUS_ROUND_TIME:
        print("You entered", guess, "\nIt took you", round(total_time),
              "seconds to respond.")
    else:
        print("I'm sorry, you ran out of time. It took you", round(total_time),
              "seconds to respond.")
main()
