class Sentence:
    ''' COMMENTS
    '''
    def __init__(self, string):
        self.__string = string

    def get_sentence(self):
        return self.__string

    def get_words(self):
        return (self.__string).split()

    def get_length(self):
        return len(self.__string)

    def get_num_words(self):
        return len(self.__string.split())

class Sentence2:
    def __init__(self, string):
        self.__string = string
        self.__string_list = string.split()

    def get_sentence(self):
        return self.__string

    def get_words(self):
        return self.__string_list

    def get_length(self):
        return len(self.__string)

    def get_num_words(self):
        return len(self.__string_list)
