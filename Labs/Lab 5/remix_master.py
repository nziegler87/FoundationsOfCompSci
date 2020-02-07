'''
    Nathanial Ziegler
    CS 5001
    February 6, 2020
    Lab 5
'''

SONG = ['old macdonald had a farm - ee-i-ee-i-o.',
        'and on that farm he had a cow - ee-i-ee-i-o.',
        'with a moo moo here and a moo moo there',
        'here a moo - there a moo - everywhere a moo moo',
        'old macdonald had a farm - ee-i-ee-i-o.' ]

def substitute_words(song, to_replace, replace_with):
    song_copy = []
    for i in range(len(song)):
        new_line = song[i].replace(to_replace, replace_with)
        song_copy.append(new_line)

    return song_copy

def reverse_song(song):
    song_copy = []
    for i in range(len(song)):
        split_sentence = song[i].split(" ")
        song_copy.append(split_sentence)
    print(song_copy)
    i = len(song_copy)

    reverse_song = []
    while i != 0:
        reverse_song.append(song_copy[i])
        i -= 1
    print(song_copy)
