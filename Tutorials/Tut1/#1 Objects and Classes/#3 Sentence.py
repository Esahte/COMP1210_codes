class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence.split(' ')

    def get_first_word(self):
        return self.sentence[0]

    def get_all_words(self):
        return self.sentence.join(' ')

    def replace(self, index, new_word):
        if index > (len(self.sentence)): return 'Index out of bound'
        self.sentence[index] = new_word
