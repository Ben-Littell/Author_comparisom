import statistics as stats
import matplotlib.pyplot as plt
import math

# novel1 is dickens
# novel2 is hawthorne
# great expectations is dickens
# scarlet letter is Hawthorne


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


def jaccard_distance(set1, set2, word_len):
    new_set1 = set()
    new_set2 = set()
    for word in set1:
        if len(word) == word_len:
            new_set1.add(word)
    for word in set2:
        if len(word) == word_len:
            new_set2.add(word)
    union = new_set1.union(new_set2)
    intersection = new_set1.intersection(new_set2)
    distance = 1 - len(intersection)/len(union)
    return distance


def weighted_distance(dict1, dict2, word_len):
    new_set1 = set()
    new_set2 = set()
    min_list = []
    max_list = []
    for word in dict1:
        if len(word) == word_len:
            new_set1.add(word)
    for word in dict2:
        if len(word) == word_len:
            new_set2.add(word)

    new_list1 = list(new_set1)
    new_list2 = list(new_set2)
    union_set = new_set1.union(new_set2)

    for word in union_set:
        main_count = new_list1.count(word)
        novel_count = new_list2.count(word)
        if main_count >= novel_count:
            max_list.append(main_count)
            min_list.append(novel_count)
        else:
            max_list.append(novel_count)
            min_list.append(main_count)

    weighted_distance = 1 - (sum(min_list) / sum(max_list))

    print(weighted_distance)


scar = open_file('scarlet_letter.txt')
great = open_file('Great_expectations.txt')
novel1 = open_file('novel1.txt')
novel2 = open_file('novel2.txt')
great.pop('')
scar_set = set()
great_set = set()
novel1_set = set()
novel2_set = set()
for key in scar:
    scar_set.add(key)
for key in great:
    great_set.add(key)
for key in novel1:
    novel1_set.add(key)
for key in novel2:
    novel2_set.add(key)

########################################################################################################################
# Scar and Novel1 Hawthorne/Dickens
scar_novel1_5 = jaccard_distance(scar_set, novel1_set, 5)
scar_novel1_6 = jaccard_distance(scar_set, novel1_set, 6)
scar_novel1_7 = jaccard_distance(scar_set, novel1_set, 7)
scar_novel1_8 = jaccard_distance(scar_set, novel1_set, 8)
scar_novel1_9 = jaccard_distance(scar_set, novel1_set, 9)
scar_novel1_10 = jaccard_distance(scar_set, novel1_set, 10)
########################################################################################################################
# Great and Novel1 Dickens/Dickens
great_novel1_5 = jaccard_distance(great_set, novel1_set, 5)
great_novel1_6 = jaccard_distance(great_set, novel1_set, 6)
great_novel1_7 = jaccard_distance(great_set, novel1_set, 7)
great_novel1_8 = jaccard_distance(great_set, novel1_set, 8)
great_novel1_9 = jaccard_distance(great_set, novel1_set, 9)
great_novel1_10 = jaccard_distance(great_set, novel1_set, 10)
########################################################################################################################
# Scar and Novel2 Hawthorne/ Hawthorne
scar_novel2_5 = jaccard_distance(scar_set, novel2_set, 5)
scar_novel2_6 = jaccard_distance(scar_set, novel2_set, 6)
scar_novel2_7 = jaccard_distance(scar_set, novel2_set, 7)
scar_novel2_8 = jaccard_distance(scar_set, novel2_set, 8)
scar_novel2_9 = jaccard_distance(scar_set, novel2_set, 9)
scar_novel2_10 = jaccard_distance(scar_set, novel2_set, 10)
########################################################################################################################
# Great and Novel2
great_novel2_5 = jaccard_distance(great_set, novel2_set, 5)
great_novel2_6 = jaccard_distance(great_set, novel2_set, 6)
great_novel2_7 = jaccard_distance(great_set, novel2_set, 7)
great_novel2_8 = jaccard_distance(great_set, novel2_set, 8)
great_novel2_9 = jaccard_distance(great_set, novel2_set, 9)
great_novel2_10 = jaccard_distance(great_set, novel2_set, 10)
########################################################################################################################
print('normal distance')
print(great_novel1_5)
print(great_novel1_6)
print(great_novel1_7)
print(great_novel1_8)
print(great_novel1_9)
print(great_novel1_10)
print()
print(scar_novel1_5)
print(scar_novel1_6)
print(scar_novel1_7)
print(scar_novel1_8)
print(scar_novel1_9)
print(scar_novel1_10)
print('weighted distance')



