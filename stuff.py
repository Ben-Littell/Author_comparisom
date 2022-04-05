import statistics as stats
import matplotlib.pyplot as plt
import math


def open_file(filename):
    new_dict = {}
    stop_words = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as",
                  "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can",
                  "could", "did", "do", "does", "doing", "done", "down", "during", "each", "few", "for", "from", "further",
                  "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself",
                  "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it",
                  "it's", "its", "itself", "just", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on",
                  "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
                  "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
                  "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                  "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
                  "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where",
                  "where's", "which", "while", "who", "who's", "whom", "will", "why", "why's", "with", "would", "you",
                  "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
    with open(filename) as file:
        text = file.readlines()
        for line in text:
            s_line = line.split()
            if len(s_line) > 0:
                if s_line[0] == 'Chapter':
                    pass
                else:
                    for word in s_line:
                        new_word = ''
                        for char in word:
                            if char.isalpha():
                                new_word += char
                        if new_word.lower() in stop_words:
                            pass
                        else:
                            if new_word.lower() in new_dict:
                                new_dict[new_word.lower()] += 1
                            else:
                                new_dict.update({new_word.lower(): 1})
        return new_dict


scar = open_file('scarlet_letter.txt')
great = open_file('Great_expectations.txt')
print(great)
print()
print(scar)

