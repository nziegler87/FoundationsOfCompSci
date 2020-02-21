with open("tempConv.txt", "w") as outfile:
    line = outfile.write("{0:^15s}-{1:^15s}\n".format("Fahrenheit", "Celsius"))
    for i in range(-300, 213):
        celsius = (i - 32) * (5/9)
        line = outfile.write("{0:^15.1f}|{1:^15.1f}\n".format(i, celsius))
