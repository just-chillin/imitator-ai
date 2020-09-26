import pandas as pd
from heapq import heappush, heappop

class Word:
    def add_chained(self, text: str):
        pass

    def __init__(self, text):
        self.text = text
        self.chain = []

def get_words_dict(fname):
    words_dict = {}
    for line in open(fname):
        for word in line:
            word = Word(word)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = []
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
