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

class Sentence3:
    def __init__(self, string):
        self.string = string

    def capitalize(self):
        self.string = self.string.upper()

    def lowercase(self):
        self.string = self.string.lower()

    def add_punctuation(self, punctuation):
        self.string = self.string + punctuation

    def __str__(self):
        return self.string
##        printable = "What a beautiful day it is! \nYour string is " + \
##                    self.string
##        return printable

    def __len__(self):
        return len("Why do I try?")
