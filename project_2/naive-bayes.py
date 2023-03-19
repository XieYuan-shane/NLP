import json
import nltk
import argparse
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from nltk.stem.porter import PorterStemmer   # from nltk.stem import PorterStemmer
import math
def compare(L,all_pro,word_pro):
    pro1 = math.log(all_pro[0])
    pro2 = math.log(all_pro[1])
    pro3 = math.log(all_pro[2])
    pro4 = math.log(all_pro[3])
    pro5 = math.log(all_pro[4])
    for i in L:
        if i in word_pro.keys():
            pro1 += math.log(word_pro[i][0])
            pro2 += math.log(word_pro[i][1])
            pro3 += math.log(word_pro[i][2])
            pro4 += math.log(word_pro[i][3])
            pro5 += math.log(word_pro[i][4])
        else:
            continue
    max1 = max(pro1,pro2,pro3,pro4,pro5)
    if pro1 == max1:
        return 'crude'
    elif pro2 == max1:
        return 'grain'
    elif pro3 == max1:
        return 'money-fx'
    elif pro4 == max1:
        return 'acq'
    else :
        return 'earn'
def preprocess(inputfile,outputfile):
    #TODO: preprocess the input file, and output the result to the output file: train.preprocessed.json,test.preprocessed.json
    #   Delete the useless symbols
    #   Convert all letters to the lowercase
    #   Use NLTK.word_tokenize() to tokenize the sentence
    #   Use nltk.PorterStemmer to stem the words
    stemmer = nltk.PorterStemmer()
    with open(inputfile, 'r') as input:
        raw_file = json.load(input)
        for article in raw_file:
            article[2] = nltk.word_tokenize(article[2])
            words = [token.lower() for token in article[2] if token.isalnum()]#token.isalnum()如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
            article[2] = [stemmer.stem(word) for word in words] # 词干提取
        with open(outputfile, 'w') as output:
            json.dump(raw_file, output)
        input.close()
        output.close()
    return
def count_word(inputfile,outputfile):
    #TODO: count the words from the corpus, and output the result to the output file in the format required.
    #   A dictionary object may help you with this work.
    #TODO: count the words from the corpus, and output the result to the output file in the format required.
    #   A dictionary object may help you with this work.
    with open(inputfile,'r') as input:
        file_contents = json.load(input) 
        crude_count = {}
        grain_count = {}
        money_count = {}
        acq_count = {}
        earn_count = {}
        all = [0,0,0,0,0]

        for i in range(0, len(file_contents)):
            if file_contents[i][1] == 'crude':
                all[0] += 1
                for crude_key in file_contents[i][2]:
                        crude_count[crude_key] = crude_count.get(crude_key, 0) + 1
            if file_contents[i][1] == 'grain':
                all[1] += 1
                for grain_key in file_contents[i][2]:
                        grain_count[grain_key] = grain_count.get(grain_key, 0) + 1
            if file_contents[i][1] == 'money-fx':
                all[2] += 1
                for money_key in file_contents[i][2]:
                        money_count[money_key] = money_count.get(money_key, 0) + 1
            if file_contents[i][1] == 'acq':
                all[3] += 1
                for acq_key in file_contents[i][2]:
                        acq_count[acq_key] = acq_count.get(acq_key, 0) + 1
            if file_contents[i][1] == 'earn':
                all[4] += 1
                for earn_key in file_contents[i][2]:
                        earn_count[earn_key] = earn_count.get(earn_key, 0) + 1   
        all_count = dict(Counter(crude_count)+Counter(grain_count)+Counter(money_count)+Counter(acq_count)+Counter(earn_count))
        with open(outputfile, 'a') as output:
            output.write("Word_count.txt:\n")
            output.write("{} {} {} {} {}\n".format(all[0],all[1],all[2],all[3],all[4]))
            for j in all_count.keys():
                output.write("{} {} {} {} {} {}\n".format(j,crude_count.get(j, 0),grain_count.get(j, 0),money_count.get(j, 0),
                                                    acq_count.get(j, 0),earn_count.get(j, 0)) )   
    input.close()
    output.close()
    return
def feature_selection(inputfile,threshold,outputfile):
    #TODO: Choose the most frequent 10000 words(defined by threshold) as the feature word
    # Use the frequency obtained in 'word_count.txt' to calculate the total word frequency in each class.
    #   Notice that when calculating the word frequency, only words recognized as features are taken into consideration.
    # Output the result to the output file in the format required
    C = {} # 一个空字典用于存放字符数量
    L = {} # 这个用于存放文件读取的内容和C
    all1 = 0
    all2 = 0
    all3 = 0
    all4 = 0
    all5 = 0
    with open(inputfile,'r') as input:
        with open(outputfile,'a') as output:
            count = 0
            input.readline()
            input.readline()
            while True:
                line1 = input.readline()#rendline()每次读取一行)
                if line1:
                    line1 = line1.replace("\n", '') #去除每一行末尾的换行符
                    x = line1.split(' ')
                    for i in range(1,6):
                       x[i] = int(x[i])#拆分文本出来的是字符，要转为整型                        
                    C[x[0]] = x[1] + x[2] + x[3] + x[4] + x[5] 
                    L[x[0]] = [x[1], x[2], x[3], x[4], x[5]]
                else:
                    break
            C= dict(sorted(C.items(), key=lambda item: item[1],reverse=True)) # 排序
            for k in C.keys():
                    all1 += L[k][0]
                    all2 += L[k][1]
                    all3 += L[k][2]
                    all4 += L[k][3]
                    all5 += L[k][4]
                    count += 1
                    if count == threshold:
                         break
            output.write("Word_dict.txt:\n")
            output.write("{} {} {} {} {}\n".format(all1, all2, all3,all4,all5))
            count = 0
            for k in C.keys():
                 output.write("{} {} {} {} {} {}\n".format(k,L[k][0],L[k][1],L[k][2],L[k][3],L[k][4]))
                 count += 1
                 if count == threshold:
                    break
    input.close()
    output.close()
    return
def calculate_probability(word_count,word_dict,outputfile):
    #TODO: Calculate the posterior probability of each feature word, and the prior probability of the class.
    #   Output the result to the output file in the format required
    #   Use 'word_count.txt' and ‘word_dict.txt’ jointly.
    with open(word_dict,'r') as input1:
        with open(word_count,'r') as input2:
            with open(outputfile,'w') as output:
                output.write("word_probability.txt:\n")
                input2.readline()
                line1 = input2.readline()
                line1 = line1.replace("\n", '') #去除每一行末尾的换行符
                x = line1.split(' ')
                for i in range(0,5):
                    x[i] = int(x[i])#拆分文本出来的是字符，要转为整型  
                all = x[0] + x[1] + x[2] + x[3] + x[4]
                output.write("{} {} {} {} {}\n".format(x[0]/all, x[1]/all, x[2]/all, x[3]/all, x[4]/all))
                input1.readline()
                first_line = input1.readline()
                first_line = first_line.replace("\n", '') #去除每一行末尾的换行符
                a = [int(z) for z in first_line.strip().split()]
                while True:
                    line_other = input1.readline()
                    if line_other:
                        line_other = line_other.replace("\n", '') #去除每一行末尾的换行符
                        y = line_other.split(' ')
                        for i in range(1,6):
                            y[i] = int(y[i])#拆分文本出来的是字符，要转为整型
                        #在这里add1 smooth
                        output.write("{} {} {} {} {} {}\n".format(y[0], (y[1]+1)/(a[0]+10000), (y[2]+1)/(a[1]+10000), 
                                                                    (y[3]+1)/(a[2]+10000), (y[4]+1)/(a[3]+10000),(y[5]+1)/(a[4]+10000)))
                    else:
                        break
    input1.close()
    input2.close()
    output.close()
    return
def classify(probability,testset,outputfile):
    #TODO: Implement the naïve Bayes classifier to assign class labels to the documents in the test set.
    #   Output the result to the output file in the format required
    word_pro = {}
    with open(probability,'r') as probability1:
        probability1.readline()
        line1 = probability1.readline()
        line1 = line1.replace("\n", '') #去除每一行末尾的换行符
        all_pro = line1.split(' ')
        for i in range(0,5):
            all_pro[i] = float(all_pro[i])
        while True:
            line_other = probability1.readline()
            if line_other:
                line_other = line_other.replace("\n", '') #去除每一行末尾的换行符
                other = line_other.split(' ')
                for i in range(1,6):
                    other[i] = float(other[i])
                word_pro[other[0]] = [other[1],other[2],other[3],other[4],other[5]]
            else:
                break
    with open(testset,'r') as test_set:
        with open(outputfile,'a') as output:
            output.write("classification_result.txt:\n")
            file_contents = json.load(test_set) 
            for i in range(len(file_contents)):
                output.write("{} {}\n".format(file_contents[i][0],compare(file_contents[i][2],all_pro,word_pro)))
    test_set.close()
    output.close()
    probability1.close()
    return
def f1_score(testset,classification_result):
    #TODO: Use the F_1 score to assess the performance of the implemented classification model
    #   The return value should be a float object.
    TP = [0,0,0,0,0]#预测此类并且对
    FP = [0,0,0,0,0]#预测此类但是错
    FN = [0,0,0,0,0]#预测其他类错
    TN = [0,0,0,0,0]#预测其他类对
    P = [0,0,0,0,0]
    R = [0,0,0,0,0]
    i = -1
    with open(testset,'r') as test:
        with open(classification_result) as result:
            test_content = json.load(test)
            result.readline()
            while True:
                line1 = result.readline()
                if line1:
                    i = i + 1
                    line1 = line1.replace("\n", '') #去除每一行末尾的换行符
                    x = line1.split(' ')
                    if(test_content[i][1] == 'crude'):
                        if(x[1] == 'crude'):
                            TP[0]+=1
                            TN[1]+=1
                            TN[2]+=1
                            TN[3]+=1
                            TN[4]+=1
                        else:
                            FP[0]+=1
                            FN[1]+=1
                            FN[2]+=1
                            FN[3]+=1
                            FN[4]+=1
                    elif(test_content[i][1] == 'grain'):
                        if(x[1] == 'grain'):
                            TP[1]+=1
                            TN[0]+=1
                            TN[2]+=1
                            TN[3]+=1
                            TN[4]+=1
                        else:
                            FP[1]+=1
                            FN[0]+=1
                            FN[2]+=1
                            FN[3]+=1
                            FN[4]+=1
                    elif(test_content[i][1] == 'money-fx'):
                        if(x[1] == 'money-fx'):
                            TP[2]+=1
                            TN[1]+=1
                            TN[0]+=1
                            TN[3]+=1
                            TN[4]+=1
                        else:
                            FP[2]+=1
                            FN[1]+=1
                            FN[0]+=1
                            FN[3]+=1
                            FN[4]+=1
                    elif(test_content[i][1] == 'acq'):
                        if(x[1] == 'acq'):
                            TP[3]+=1
                            TN[1]+=1
                            TN[2]+=1
                            TN[0]+=1
                            TN[4]+=1
                        else:
                            FP[3]+=1
                            FN[1]+=1
                            FN[2]+=1
                            FN[0]+=1
                            FN[4]+=1
                    elif(test_content[i][1] == 'earn'):
                        if(x[1] == 'earn'):
                            TP[4]+=1
                            TN[1]+=1
                            TN[2]+=1
                            TN[3]+=1
                            TN[0]+=1
                        else:
                            FP[4]+=1
                            FN[1]+=1
                            FN[2]+=1
                            FN[3]+=1
                            FN[0]+=1    
                else:
                    break
        F1=[0,0,0,0,0]
        for i in range(5):
            P[i] = TP[i]/(TP[i]+FP[i])
            R[i] = TP[i]/(TP[i]+FN[i])
        
        P_ave = (P[0]+P[1]+P[2]+P[3]+P[4])/5
        R_ave = (R[0]+R[1]+R[2]+R[3]+R[4])/5
        F1 = (2*P_ave*R_ave)/(P_ave+R_ave)
        
        
    return F1
def main():
    ''' Main Function '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-pps', '--preprocess',type=str,nargs=2,help='preprocess the dataset')
    parser.add_argument('-cw','--count_word',type=str,nargs=2,help='count the words from the corpus')
    parser.add_argument('-fs','--feature_selection',type=str,nargs=3,help='\select the features from the corpus')
    parser.add_argument('-cp','--calculate_probability',type=str,nargs=3,
                        help='calculate the posterior probability of each feature word, and the prior probability of the class')
    parser.add_argument('-cl','--classify',type=str,nargs=3,
                        help='classify the testset documents based on the probability calculated')
    parser.add_argument('-f1','--f1_score', type=str, nargs=2,
                        help='calculate the F-1 score based on the classification result.')
    opt=parser.parse_args()

    if(opt.preprocess):
        input_file = opt.preprocess[0]
        output_file = opt.preprocess[1]
        preprocess(input_file,output_file)
    elif(opt.count_word):
        input_file = opt.count_word[0]
        output_file = opt.count_word[1]
        count_word(input_file,output_file)
    elif(opt.feature_selection):
        input_file = opt.feature_selection[0]
        threshold = int(opt.feature_selection[1])
        outputfile = opt.feature_selection[2]
        feature_selection(input_file,threshold,outputfile)
    elif(opt.calculate_probability):
        word_count = opt.calculate_probability[0]
        word_dict = opt.calculate_probability[1]
        output_file = opt.calculate_probability[2]
        calculate_probability(word_count,word_dict,output_file)
    elif(opt.classify):
        probability = opt.classify[0]
        testset = opt.classify[1]
        outputfile = opt.classify[2]
        classify(probability,testset,outputfile)
    elif(opt.f1_score):
        testset = opt.f1_score[0]
        classification_result = opt.f1_score[1]
        f1 = f1_score(testset,classification_result)
        print('The F1 score of the classification result is: '+str(f1))


if __name__ == '__main__':
    import os
    main()