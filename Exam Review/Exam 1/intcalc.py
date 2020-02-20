user_int = int(input("Enter a positive integer. I will then calculate the " +
                     "sum of the integers.\n"))

user_sum = 0

for i in range(user_int + 1):
    user_sum += (2 * i)

print(user_sum)
