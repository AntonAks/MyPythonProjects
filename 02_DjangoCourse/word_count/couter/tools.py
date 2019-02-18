class Text:
    def __init__(self, content):
        self.content = content
        self.content_clean = self.get_clean_content()
        self.words_list = self.content_clean.split()
        self.words_set = set(self.words_list)
        self.number_of_words = self.words_list.__len__()
        self.number_of_unique_words = self.words_set.__len__()
        self.words = self.get_words()


    def get_words(self):
        words_dict = {}

        for w in self.words_set:
            words_dict[w] = list(self.words_list).count(w)

        words_dict = sorted(words_dict.items(), key=lambda words_dict: words_dict[1], reverse=True)
        return words_dict


    def get_clean_content(self):
        symbols_for_replace = [',', '.', '--', '/', '|', '?', '!', ':', ';']
        content_clean = self.content
        for s in symbols_for_replace:
            content_clean = content_clean.replace(s,' ')

        return content_clean
