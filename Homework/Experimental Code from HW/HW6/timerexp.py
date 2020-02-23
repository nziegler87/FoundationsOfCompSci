import time, threading

BONUS_ROUND_TIME = 20

def countdown():
    global my_timer

    my_timer = BONUS_ROUND_TIME

    for i in range(my_timer):
        my_timer -= 1
        time.sleep(1)
    return my_timer
    
def main():
    print("You have", BONUS_ROUND_TIME, "seconds to enter "
          "your guess...starting now.")
    time = threading.Thread(target=countdown)
    time.start()
    guess = input("Enter your guess: ")

    if my_timer == 0:
        print("I'm sorry. You ran out of time.")
    else:
        print("You entered:", guess, "\nYou had", my_timer, "seconds left.")

main()
