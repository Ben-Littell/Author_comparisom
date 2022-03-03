import statistics as stats
import math
import matplotlib.pyplot as plt


def graph_gaussian(mean1, mean2, SD1, SD2, variance1, variance2):
    y_list1 = []
    x_list1 = []
    y_list2 = []
    x_list2 = []
    x_start1 = mean1 - 1.5 * SD1
    delta_x1 = (3 * SD1) / 100
    m_s1 = mean1 - SD1
    mps1 = mean1 + SD1
    x_start2 = mean1 - 1.5 * SD2
    delta_x2 = (3 * SD2) / 100
    m_s2 = mean2 - SD2
    mps2 = mean2 + SD2

    # COMPUTE FOR FILE 1
    for i in range(100):
        x = i * delta_x1 + x_start1
        y = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((x - mean1) ** 2) / (2 * variance1))
        y_list1.append(y)
        x_list1.append(x)
        y_left = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((m_s1 - mean1) ** 2) / (2 * variance1))
        Left1 = y_left
        y_right = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((mps1 - mean1) ** 2) / (2 * variance1))
        Right1 = y_right

    apex1 = max(y_list1)
    plt.plot(x_list1, y_list1, '-b')
    plt.plot([mean1, mean1], [0, apex1], '-c')
    plt.plot([mean1 - SD1, mean1 - SD1], [0, Left1], '-c')
    plt.plot([mean1 + SD1, mean1 + SD1], [0, Right1], '-c')


    # COMPUTE FOR FILE 2
    for i in range(100):
        x = i * delta_x2 + x_start2
        y = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((x - mean2) ** 2) / (2 * variance2))
        y_list2.append(y)
        x_list2.append(x)
        y_left = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((m_s2 - mean2) ** 2) / (2 * variance2))
        Left2 = y_left
        y_right = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((mps2 - mean2) ** 2) / (2 * variance2))
        Right2 = y_right

    apex2 = max(y_list2)
    plt.plot(x_list2, y_list2, '-k')
    plt.plot([mean2, mean2], [0, apex2], '-r')
    plt.plot([mean2 - SD2, mean2 - SD2], [0, Left2], '-r')
    plt.plot([mean2 + SD2, mean2 + SD2], [0, Right2], '-r')

    plt.legend(['Great Expectations', 'Scarlet Letter'], loc='upper right')
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
great_sen_list,  great_par_len, great_word_sen = open_file('Great_expectations.txt')


graph_gaussian(stats.mean(scar_sen_list), stats.mean(great_sen_list), stats.stdev(scar_sen_list),
               stats.stdev(great_sen_list), stats.variance(scar_sen_list), stats.variance(great_sen_list))
graph_gaussian(stats.mean(scar_par_len), stats.mean(great_par_len), stats.stdev(scar_par_len),
               stats.stdev(great_par_len), stats.variance(scar_par_len), stats.variance(great_par_len))
graph_gaussian(stats.mean(scar_word_sen), stats.mean(great_word_sen), stats.stdev(scar_word_sen),
               stats.stdev(great_word_sen), stats.variance(scar_word_sen), stats.variance(great_word_sen))

