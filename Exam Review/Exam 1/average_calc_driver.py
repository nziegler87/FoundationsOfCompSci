from average_calc_functions import collect_number, append_list, calculate_mean

total_list = []
while True:
    number = collect_number()
    if number == 0:
        break
    else:
        append_list(number, total_list)

mean = calculate_mean(total_list)
print("The average of your numbers was", mean)
