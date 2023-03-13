#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# --------------------------------------------------
# Description:  A starter code
# --------------------------------------------------
# Author: Wang-SongSheng <wang.songsheng@connect.um.edu.mo>
# Created Date : March 4th 2021, 12:00:00
# --------------------------------------------------

import argparse
import numpy as np

def word_edit_distance(x, y):
    # implement the dynamic programming algorithm to calculate the edit distance and alignment between two words.
    # input: two strings x and y
    # output:
    # edit_distance: int
    # alignment: a list which indicates the alignment between each letter
    # the following is an example of the return value
    str1 = '#' + x
    str2 = '#' + y
    len1 = len(str1)
    len2 = len(str2)
    # 记录开销的矩阵
    solutionmatrix = np.zeros((len2, len1))

    # 初始化
    for i in range(0, len1):
        solutionmatrix[0][i] = i
    for i in range(0, len2):
        solutionmatrix[i][0] = i

    # 记录路径的矩阵,并初始化之前初始化的路径
    # 数字3表示添加，数字4表示删除

    recordmatrix1 = np.zeros((len2, len1))
    for i in range(0, len1):
        recordmatrix1[0][i] = 4
    for i in range(0, len2):
        recordmatrix1[i][0] = 3
    recordmatrix1[0][0] = 100  # 回溯终止符

    # 判断两个字符串当前位置是否相等
    for i in range(1, len1):
        for j in range(1, len2):
            if str1[i] == str2[j]:
                cost = 0
            else:
                cost = 2

            # 计算开销
            substitute = solutionmatrix[j - 1][i - 1] + cost
            delete = solutionmatrix[j][i - 1] + 1
            insert = solutionmatrix[j - 1][i] + 1
            solutionmatrix[j][i] = min(substitute, insert,delete)

            prior1 = [substitute, insert,delete]  # 替换优于添加
            whichone1 = prior1.index(min(prior1))

            # 记录【i，j】是怎么变化而来的  2=替换，3=添加，4=删除，5=保留
            if whichone1 == 0 and cost == 2:
                recordmatrix1[j][i] = 2
            elif whichone1 == 0 and cost == 0:
                recordmatrix1[j][i] = 5
            elif whichone1 == 1:
                recordmatrix1[j][i] = 3
            else:
                recordmatrix1[j][i] = 4

    # 回溯路径
    alignment = [[], []]
    i1 = len1 - 1
    j1 = len2 - 1
    temp1 = recordmatrix1[j1][i1]

    while temp1 != 100:
        if temp1 == 2:  # 2表示substitute
            alignment[1].append(str2[j1])
            alignment[0].append(str1[i1])
            i1 = i1 - 1
            j1 = j1 - 1

        elif temp1 == 5:  # 5表示保留
            alignment[1].append(str2[j1])
            alignment[0].append(str1[i1])
            i1 = i1 - 1
            j1 = j1 - 1

        elif temp1 == 3:  # 3表示添加
            alignment[1].append("{}".format(str2[j1]))
            alignment[0].append("{}".format('-'))
            j1 = j1 - 1

        elif temp1 == 4:
            alignment[1].append("{}".format('-'))
            alignment[0].append("{}".format(str1[i1]))
            i1 = i1 - 1

        temp1 = recordmatrix1[j1][i1]

    alignment[0].reverse()
    alignment[1].reverse()

    min_distance = int(solutionmatrix[len2 - 1][len1 - 1])

    return min_distance, alignment


def sentence_edit_distance(x, y):
    if not isinstance(x, list):  # 判断是否为列表
        str1 = x.split()
        str2 = y.split()
    else:
        str1 = x
        str2 = y
        # 先将两个字符串分割成一个列表
    str1.insert(0, '#')
    str2.insert(0, '#')
    len1 = len(str1)
    len2 = len(str2)
    # 记录开销的矩阵
    solutionmatrix = np.zeros((len2, len1))

    # 初始化
    for i in range(0, len1):
        solutionmatrix[0][i] = i
    for i in range(0, len2):
        solutionmatrix[i][0] = i

    # 记录路径的矩阵,并初始化之前初始化的路径
    # 数字3表示添加，数字4表示删除

    recordmatrix1 = np.zeros((len2, len1))
    for i in range(0, len1):
        recordmatrix1[0][i] = 4
    for i in range(0, len2):
        recordmatrix1[i][0] = 3
    recordmatrix1[0][0] = 100  # 回溯终止符

    # 判断两个字符串当前位置是否相等
    for i in range(1, len1):
        for j in range(1, len2):
            if str1[i] == str2[j]:
                cost = 0
            else:
                cost = 2

            # 计算开销
            substitute = solutionmatrix[j - 1][i - 1] + cost
            delete = solutionmatrix[j][i - 1] + 1
            insert = solutionmatrix[j - 1][i] + 1
            solutionmatrix[j][i] = min(substitute, insert, delete)

            # 记录路径，操作的优先级不同，路径也不同，这里仅拿两种优先级举例
            prior1 = [substitute, insert, delete]  # 替换优于添加
            whichone1 = prior1.index(min(prior1))

            # 记录【i，j】是怎么变化而来的  2=替换，3=添加，4=删除，5=保留
            if whichone1 == 0 and cost == 2:
                recordmatrix1[j][i] = 2
            elif whichone1 == 0 and cost == 0:
                recordmatrix1[j][i] = 5
            elif whichone1 == 1:
                recordmatrix1[j][i] = 3
            else:
                recordmatrix1[j][i] = 4

    # 回溯路径
    alignment = [[], []]
    i1 = len1 - 1
    j1 = len2 - 1
    temp1 = recordmatrix1[j1][i1]

    while temp1 != 100:
        if temp1 == 2:  # 2表示substitute
            alignment[1].append(str2[j1])
            alignment[0].append(str1[i1])
            i1 = i1 - 1
            j1 = j1 - 1

        elif temp1 == 5:  # 5表示保留
            alignment[1].append(str2[j1])
            alignment[0].append(str1[i1])
            i1 = i1 - 1
            j1 = j1 - 1

        elif temp1 == 3:  # 3表示添加
            alignment[1].append("{}".format(str2[j1]))
            alignment[0].append("{}".format('-'))
            j1 = j1 - 1

        elif temp1 == 4:
            alignment[1].append("{}".format('-'))
            alignment[0].append("{}".format(str1[i1]))
            i1 = i1 - 1

        temp1 = recordmatrix1[j1][i1]

    alignment[0].reverse()
    alignment[1].reverse()

    min_distance = int(solutionmatrix[len2 - 1][len1 - 1])

    return min_distance, alignment


def sentence_preprocess(sentence):
    # temporarily preprocess the sentence string input from the command line
    # input: a string sentence
    # output: the tokenized sentence (a list, each item corresponds to a word or a punctuation of the sentence)
    sentence = sentence.split()
    return sentence


def output_alignment(alignment):
    # output the alignment in the format required
    if len(alignment[0]) != len(alignment[1]):
        print('ERROR: WRONG ALIGNMENT FORMAT')
        input()
        exit(0)
    print('An possible alignment is:')
    merged_matrix = alignment[0] + alignment[1]
    max_len = 0
    for item in merged_matrix:
        if len(item) > max_len:
            max_len = len(item)
    for i in range(len(alignment[0])):
        print(alignment[0][i].rjust(max_len) + ' ', end=''),
    print('')
    for i in range(len(alignment[0])):
        print(('|').rjust(max_len) + ' ', end=''),
    print('')
    for i in range(len(alignment[1])):
        print(alignment[1][i].rjust(max_len) + ' ', end='')
    print('')
    return


def batch_word(inputfile, outputfile):
    # implement the function to finish the requirement 3 TODO: read the samples from the input file (i.e.
    #  word_corpus.txt), notice that the number of the hypothesis is maybe diverse use the function
    #  word_edit_distance to calculate the edit distance between the reference hand each hypothesis output the result
    #  in the file 'word_edit_distance.txt' with the required format
    with open(inputfile, 'r',encoding = 'UTF-8') as f:
        with open(outputfile, 'a',encoding = 'UTF-8') as output:
            lines = f.readlines()
            for line in lines:
                word = line.split()
                if word[0] == 'R':
                    str1 = word[1]
                    output.write(line)
                    continue

                elif word[0] == 'H':
                    str2 = word[1]
                    distance,alignment = word_edit_distance(str1, str2)
                    output.write("{} {} \n".format(line.rstrip(), distance))
    f.close()
    output.close()
    return


def batch_sentence(inputfile,outputfile):
    # implement the function to finish the requirement 4
    # TODO:
    #   read the samples from the input file (i.e. sentence_corpus.txt)
    #   use the function sentence_edit_distance to calculate the edit distance between the reference hand each hypothesis
    #   output the result in the file 'sentence_edit_distance.txt' with the required format
    with open(inputfile, 'r',encoding = 'UTF-8') as f:
        with open(outputfile, 'a',encoding = 'UTF-8') as output:
            lines = f.readlines()  # rendlines()读取全部行，每行都转化为列表中的一项
            for line in lines:
                word = line.split()
                if (word[0] == 'R'):
                    str1 = []
                    for i in range(1, len(word)):
                        str1.append(word[i])
                    output.write(line)
                    continue

                elif (word[0] == 'H'):
                    str2 = []
                    for i in range(1, len(word)):
                        str2.append(word[i])
                    a, b = sentence_edit_distance(str1, str2)
                    del str1[0]
                    output.write("{} {} \n".format(line.rstrip(), a))
    f.close()
    output.close()
    return


def main():
    """ Main Function """

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word', type=str, nargs=2, help='word comparson')
    parser.add_argument('-s', '--sentence', type=str, nargs=2, help='sentence comparison')
    parser.add_argument('-bw', '--batch_word', type=str, nargs=2, help='batch word comparison,input the filename')
    parser.add_argument('-bs', '--batch_sentence', type=str, nargs=2, help='batch word comparison,input the filename')

    opt = parser.parse_args()

    if opt.word:
        edit_distance, alignment = word_edit_distance(opt.word[0], opt.word[1])
        print('The cost is: ' + str(edit_distance))
        output_alignment(alignment)
    elif opt.sentence:
        edit_distance, alignment = sentence_edit_distance(sentence_preprocess(opt.sentence[0]),
                                                          sentence_preprocess(opt.sentence[1]))
        print('The cost is: ' + str(edit_distance))
        output_alignment(alignment)
    elif opt.batch_word:
        batch_word(opt.batch_word[0], opt.batch_word[1])
    elif opt.batch_sentence:
        batch_sentence(opt.batch_sentence[0], opt.batch_sentence[1])


if __name__ == '__main__':
    import os

    main()
