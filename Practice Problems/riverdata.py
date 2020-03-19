with open("riverdata.txt", "r") as infile:
    data = []
    for line in infile.readlines():
        data.append(line)

    print(data)
