import time, threading
 
def countdown():
    global my_timer

    my_timer = 5

    for i in range(5):
        my_timer -= 1
        time.sleep(1)

    print("Out of time")
    
def main():
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()
    while my_timer > 0:
        print(my_timer)
        time.sleep(1)

    print("Time up")

main()
