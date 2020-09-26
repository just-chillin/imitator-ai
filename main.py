from __future__ import annotations

import string
from collections import defaultdict
from typing import Mapping
from ftfy import fix_text

BANNED_WORDS = ["RT", "AUDIENCE:"]


class Word:

    def is_end_of_sentence(self):
        return self.text[-1] in ['!', '.', '?']

    def most_frequent(self) -> Word:
        if len(self.chain.items()) == 0:
            return Word('.')
        return max(self.chain.items(), key=lambda w: w[1])[0]

    def add_word(self, word: Word):
        self.chain[word] += 1

    def print_sentence(self):
        if self.is_end_of_sentence():
            return self.text + '\n'
        elif self.chain == {}:
            return self.text + ' '
        return self.text + ' ' + self.most_frequent().print_sentence()

    def __init__(self, word: str):
        self.text = fix_text(word)
        self.chain: Mapping[Word, int] = defaultdict(lambda: 0)

    def __str__(self):
        return self.text

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        if type(other) == Word:
            return self.text == other.text
        else:
            return self.text == other


def is_valid_word(w: str):
    return w != '' \
           and w[0] not in ["("] \
           and w[-1] != ':' \
           and w not in BANNED_WORDS \
           and not w.startswith("http")


def get_words_dict(fname):
    words = dict()
    for line in open(fname, errors='ignore'):
        line = list(filter(lambda w: is_valid_word(w), line.strip().split(' ')))
        for i in range(len(line) - 1):
            word, next_word = Word(line[i]), Word(line[i + 1])
            if word not in words:
                words[word] = word
            words[word].add_word(next_word)
    return words


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    skip_next_word = False
    for k in get_words_dict('./trump-tweets.txt'):
        if skip_next_word:
            skip_next_word = False
            continue
        if k.text[0] in string.ascii_uppercase:
            sentence = k.print_sentence()
            if not sentence.endswith("\n"):
                skip_next_word = True
            print(sentence, end='')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
