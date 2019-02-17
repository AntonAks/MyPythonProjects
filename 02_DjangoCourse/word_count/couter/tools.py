class Text:
    def __init__(self, content):
        self.content = content
        self.number_of_words = get_number_of_words()
        self.number_of_unique_words = get_number_of_words()
        self.words = {}


    def get_number_of_words(self):
        return str(self.content).split().__len__()


    def get_words_and_frequency():
        pass
