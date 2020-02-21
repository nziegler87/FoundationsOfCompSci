with open("rainfall.txt", "r") as infile:
    with open("rainfallFmt.txt", "w") as outfile:

        for line in infile:
            value = line.split(",")
            
            city = value[0]
            rainfall = float(value[1])

            newline = outfile.write("{0:>25s}{1:^5.1f}"
                                    "\n".format(city, rainfall))
            
