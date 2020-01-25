def average(N):
    sum = 0
    count = 0
    for x in range(1, N+1):
        sum += x
        count += 1
    avg = sum / count
    print(avg)
