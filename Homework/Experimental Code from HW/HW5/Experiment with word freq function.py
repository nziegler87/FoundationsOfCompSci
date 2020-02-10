JAKE = ['I work best alone except when it comes to sex but sometimes including sex', 'I love your face and I love your butt', 'For the last time orangina is not orange soda', "That's where the blood's supposed to be", "I'd like your eight dollarest bottlest of wine please", 'Title of your sex tape', 'Guys Captain Holt has no pants on', "I'm fancy one time I had coffee flavored ice cream", "You know how I'm kind of a sexy bad boy", 'You are orangina and I am orange soda']

def calculate_word_frequency(word_list):
    ''' Name: calculate_word_frequency
        Input: List of strings
        Returns: nested list formated: [["word", count],["word", count]]
                 "word" = string and count = int
        Does: Counts frequency of word usage in word_list and returns
              nested list
    '''
    count_list = []
    
    # iterate through each word in list
    for word in word_list:
            
        # if word in count_list, increase word count by one in nested list
        if check_nested_list(word, count_list, 0):
            index = search_nested_list(word, count_list, 0)
            count_list[index][1] += 1
            
        # if no previous conditions true, add word to list with count 1
        else:
            count_list = append_to_nested(count_list, word)

    return count_list
