import statistics as stats
import math
import matplotlib.pyplot as plt


def gaussian_calculation(mean, standard_dev, variance):
    y_list = []
    x_list = []
    x_start = mean - 1.5 * standard_dev
    delta_x = (3 * standard_dev) / 100
    m_s = mean - standard_dev
    mps = mean + standard_dev
    for i in range(100):
        x = i * delta_x + x_start
        y = (1 / (standard_dev * math.sqrt(2 * math.pi))) * math.e ** - (((x - mean) ** 2) / (2 * variance))
        y_list.append(y)
        x_list.append(x)

        y_left = (1 / (standard_dev * math.sqrt(2 * math.pi))) * math.e ** - (((m_s - mean) ** 2) / (2 * variance))
        Left = y_left

        y_right = (1 / (standard_dev * math.sqrt(2 * math.pi))) * math.e ** - (((mps - mean) ** 2) / (2 * variance))
        Right = y_right

    plt.axis([mean - (1.5 * standard_dev), mean + (1.5 * standard_dev), min(y_list), max(y_list)])
    apex = max(y_list)
    plt.plot(x_list, y_list, '-b')
    plt.plot([mean, mean], [0, apex], '-r')
    plt.plot([mean - standard_dev, mean - standard_dev], [0, Left], '-r')
    plt.plot([mean + standard_dev, mean + standard_dev], [0, Right], '-r')
    plt.show()


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
        word_sen = []
        for val in text1_s:
            w_counter += 1
            for char in val:
                if char in punc_list:
                    word_sen.append(w_counter)
                    w_counter = 0
        # mean_word_sen = stats.mean(word_sen)
        # std_words_sen = stats.mean(word_sen)
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

        # mean_sen_par = stats.mean(sentence_list)
        # std_sen_par = stats.stdev(sentence_list)
        # words_par_mean = stats.mean(par_len_list)
        # words_par_std = stats.stdev(par_len_list)
    return sentence_list, par_len_list, word_sen


scar_sen_list, scar_par_len, scar_word_sen = open_file('scarlet_letter.txt')
great_sen_list,  gwords_par_mean, gwords_par_std, gmean_word_sen, gstd_words_sen = \
    open_file('Great_expectations.txt')


print(smean_sen_par, sstd_sen_par, swords_par_mean, swords_par_std, smean_word_sen, sstd_words_sen, sep='\n')
print()
print(gmean_sen_par, gstd_sen_par, gwords_par_mean, gwords_par_std, gmean_word_sen, gstd_words_sen, sep='\n')



