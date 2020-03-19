with open("starspangledbanner.txt", "r") as infile:
    poem = infile.read().lower().split()

word_count = {}

for word in poem:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

top_words = sorted(word_count, key = word_count.__getitem__, reverse = True)
top_five = top_words[:5]                  

print("The top five words are:")

for count, word in enumerate(top_five, start = 1):
    print("  ", count, ". ", word, sep = "")



    




