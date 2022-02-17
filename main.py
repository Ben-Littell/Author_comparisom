import statistics as stats
import math


def open_file(filename):
    new_dict = {}
    paragraph_list = []
    par_len_list = []
    sentence_list = []
    sentence_counter = 0
    new_str = ''
    end_sentence = ['.', '!', '?']
    with open(filename) as file:
        text = file.read()
        chapter_list = text.split('Chapter ')
        chapter_list.pop(0)
        text1_s = text.split()
        punc_list = ['.', '!', '?', ':']
        w_counter = 0
        len_list = []
        for val in text1_s:
            w_counter += 1
            for char in val:
                if char in punc_list:
                    len_list.append(w_counter)
                    w_counter = 0
        mean_word_sen = stats.mean(len_list)
        std_words_sen = stats.mean(len_list)
    with open(filename) as file:
        text2 = file.readlines()
        for line in text2:
            row = line.split()
            if line in ['\n', '\r\n', '', '\t']:
                paragraph_list.append(new_str)
                new_str = ''
            elif len(row) >= 1:
                if row[0].lower() == 'chapter':
                    pass
                else:
                    new_str += line
        for item in paragraph_list:
            for char in item:
                if char in end_sentence:
                    sentence_counter += 1
            if sentence_counter >= 1:
                sentence_list.append(sentence_counter)
            sentence_counter = 0
            s_item = item.split()
            if len(s_item) > 0:
                par_len_list.append(len(s_item))

        mean_sen_par = stats.mean(sentence_list)
        std_sen_par = stats.stdev(sentence_list)
        words_par_mean = stats.mean(par_len_list)
        words_par_std = stats.stdev(par_len_list)
    return mean_sen_par, std_sen_par, words_par_mean, words_par_std, mean_word_sen, std_words_sen


smean_sen_par, sstd_sen_par, swords_par_mean, swords_par_std, smean_word_sen, sstd_words_sen = \
    open_file('scarlet_letter.txt')
gmean_sen_par, gstd_sen_par, gwords_par_mean, gwords_par_std, gmean_word_sen, gstd_words_sen = \
    open_file('Great_expectations.txt')
print(smean_sen_par, sstd_sen_par, swords_par_mean, swords_par_std, smean_word_sen, sstd_words_sen, sep='\n')
print()
print(gmean_sen_par, gstd_sen_par, gwords_par_mean, gwords_par_std, gmean_word_sen, gstd_words_sen, sep='\n')
