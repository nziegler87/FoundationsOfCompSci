'''
    Nathanial Ziegler
    CS 5001
    February 6, 2020
    Lab 3
'''


POEM = "Intensive technologies croon.\n\nLocal bandits lesson.\n" \
       "Old notebooks emote.\nVideos intersect.\n" \
       "Early notebooks choreograph.\n\nAsynchronous modems search.\n" \
       "Local desktops deliver.\nInteractive videos skill.\n" \
       "Grain tablets clap.\nNew technologies cry.\n\n" \
       "Commercial kits chant.\nSublingual tablets exalt.\n"

DREAM = "If tax payers tell their tale.\n" \
        "Of heated victories against the tax man.\n" \
        "A meeting with others who file late.\n\n" \
        "There were many reasons to file early...\n" \
        "Remembering what H&R Block said: 'Leave it to us!'\n" \
        "Ford cars with ejection seats - is that a valid deduction?\n\n" \
        "Peas and carrots, please - you barely ate dinner.\n" \
        "Floors covered with peas - you couldn't eat them after all.\n" \
        "Flux capacitors were science fiction - go back in time!\n\n" \
        "Flow with this - the deadline is looming.\n" \
        "Trails of paper litter your office.\n Follow the bouncing ball.\n" \
        "Follow the rabbit.\n\n Full of ideas; you're distracted again.\n" \
        "Scoops of ice cream await, finish the task!\n" \
        "Alas, you'll need an extension.\n" \
        "Rise up, go to bed - it's January and only a bad tax dream."

def print_acrostics(input_list):
    ''' Name: print_acrostics
        Inputs: list with variable and column number (int)
        Returns: nothing
    '''
    # isolate poem and column values from input list
    poem = input_list[0]
    column = input_list[1]
    
    # split string into list items using paragraph return sep
    poem_list = poem.split("\n")

    # iterate through each item in string
    for sentence in poem_list:

        # if list item is blank, print space
        if sentence == "":
            print(" ", end = "")

        # print specified column number in each string
        else:
            print(sentence[column], end = "")
    print()

def main():
    acrostics = [[POEM, 0], [DREAM, 3]]
    for each in acrostics:
        print_acrostics(each)


main()
