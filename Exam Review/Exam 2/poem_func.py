def main2():
    try:
        with open("pigs.txt", "r") as infile:
            poem = []
            for line in infile.readlines():
                poem.append(line.strip())
        print(poem)
    except OSError:
        print("I'm sorry, your file could not be read")

    


    try:
        with open("new_pigs.txt", "w") as outfile:
            for line in poem:
                outfile.write(line + "\n")
    except OSError:
        print("Your file could not be saved.")

def main():
    try:
        with open("pigs.txt", "r") as infile:
            new = []
            for line in infile.readlines():
                new.append(line.split())
        print(new)
    except OSError:
        print("Filename not found.")

    while True:
        find = input("Enter a word to find: ")
        if find == "exit":
            break
        else:
            replace = input("Enter the word to replace: ")
            for line in new:
                for i in range(len(line)):
                    if line[i] == find:
                        line[i] = replace
            print(new)

    final = ""
    for line in new:
        final += " ".join(line) + "\n"

    try:
        with open("updated_pigs.txt", "w") as infile:
            infile.write(final)
    except OSError:
        print("Your file cannot be saved")

main()
