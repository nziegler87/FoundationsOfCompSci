import time, sys

sec = 20
for i in range(sec):
    print(sec, end = " ")
    sec -= 1
    time.sleep(1)

for i in range(sec):
    sys.stdout.write(i + "\r")
    sys.stdout.flush()

