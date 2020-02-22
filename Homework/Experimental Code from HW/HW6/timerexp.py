import time

def countdown(seconds_left):
    seconds = seconds_left
    while seconds > -1:
        print(seconds, end = '\r')
        time.sleep(1)
        seconds -= 1
    break

guess = input("You have 20 seconds, starting now, to guess: ")
countdown(20)
