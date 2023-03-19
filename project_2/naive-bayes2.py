import json
import nltk
import argparse
import math

def preprocess(inputfile, outputfile):
    # TODO: preprocess the input file, and output the result to the output file: train.preprocessed.json,test.preprocessed.json
    #   Delete the useless symbols
    #   Convert all letters to the lowercase
    #   Use NLTK.word_tokenize() to tokenize the sentence
    #   Use nltk.PorterStemmer to stem the words
    preprocessed = []
    stemmer = nltk.PorterStemmer()
    with open(inputfile, 'r') as file:
        raw_file = json.load(file)
        for article in raw_file:
            id = ""
            for char in article[0]:
                if char.isdigit():
                    id += char
            words_raw = nltk.word_tokenize(article[2])
            words = [token.lower() for token in words_raw if token.isalnum()]
            word_processed = [stemmer.stem(word) for word in words]
            preprocessed_article = [id, article[1], word_processed]
            preprocessed.append(preprocessed_article)
        with open(outputfile, 'w') as file:
            json.dump(preprocessed, file)
    return

def count_word(inputfile, outputfile):
    # TODO: count the words from the corpus, and output the result to the output file in the format required.
    #   A dictionary object may help you with this work.
    categories = ['crude', 'grain', 'money-fx', 'acq', 'earn']
    categories_count = [0, 0, 0, 0, 0]
    word_count = {}
    with open(inputfile, 'r') as file:
        raw_file = json.load(file)
        for article in raw_file:
            article_categories = -1
            for i in range(5):
                if article[1] == categories[i]:
                    article_categories = i
                    break
            if (article_categories == -1):
                continue
            categories_count[article_categories] += 1
            words = article[2]
            for word in words:
                if word not in word_count:
                    word_count[word] = [0, 0, 0, 0, 0]
                word_count[word][article_categories] += 1
        with open(outputfile, 'w') as file:
            file.write(' '.join(str(num) for num in categories_count))
            file.write('\n')
            for key, values in word_count.items():
                file.write(key)
                for value in values:
                    file.write(f' {value}')
                file.write('\n')
    return


def feature_selection(inputfile, threshold, outputfile):
    # TODO: Choose the most frequent 10000 words(defined by threshold) as the feature word
    # Use the frequency obtained in 'word_count.txt' to calculate the total word frequency in each class.
    #   Notice that when calculating the word frequency, only words recognized as features are taken into consideration.
    # Output the result to the output file in the format required
    with open(inputfile, 'r') as file:
        lines = file.readlines()
    count_word = {}
    categories_count = [0, 0, 0, 0, 0]
    for line in lines[1:]:
        elements = line.strip().split(' ')
        key = elements[0]
        values = [int(x) for x in elements[1:]]
        count = 0
        for value in values:
            count = count+value
        values.append(count)
        count_word[key] = values
    sorted_items = sorted(count_word.items(),
                          key=lambda x: x[1][5], reverse=True)
    top_keys = sorted_items[:threshold]
    for i in range(5):
        for item in top_keys:
            categories_count[i] += int(item[1][i])
    with open(outputfile, 'w') as file:
        file.write(' '.join(str(num) for num in categories_count))
        file.write('\n')
        for item in top_keys:
            line = item[0] + " " + " ".join(map(str, item[1][:5]))
            file.write(line + "\n")
    return

def calculate_probability(word_count, word_dict, outputfile):
    # TODO: Calculate the posterior probability of each feature word, and the prior probability of the class.
    #   Output the result to the output file in the format required
    #   Use 'word_count.txt' and ‘word_dict.txt’ jointly.
    threshold=0
    with open(word_count, 'r') as count:
        first_lines = count.readline()
    article_number = [int(num) for num in first_lines.strip().split()]
    article_total_number=0
    article_probability=[0,0,0,0,0]
    for number in article_number:
        article_total_number+=number
    for i in range(5):
        article_probability[i]=format(article_number[i]/article_total_number,".10f")
    with open(word_dict, 'r') as dict:
        lines = dict.readlines()
    count_word = {}
    total_number = [int(num) for num in lines[0].strip().split()]
    for line in lines[1:]:
        threshold+=1
        elements = line.strip().split(' ')
        key = elements[0]
        values = [int(x) for x in elements[1:]]
        count = 0
        for value in values:
            count = count+value
        values.append(count)
        count_word[key] = values
    probability_word = {}
    for word, value in count_word.items():
        compute_probability=[0,0,0,0,0]
        for i in range(5):
            compute_probability[i]=format((value[i]+1)/(total_number[i]+threshold),".10f")
        probability_word[word]=compute_probability
    with open(outputfile, "w") as file:
        file.write(' '.join(str(num) for num in article_probability))
        file.write('\n')
        for key, values in probability_word.items():
            line = key + " " + " ".join(map(str, values))
            file.write(line + "\n")
    return


def classify(probability, testset, outputfile):
    # TODO: Implement the naïve Bayes classifier to assign class labels to the documents in the test set.
    #   Output the result to the output file in the format required
    word_prob={}
    categories = ['crude', 'grain', 'money-fx', 'acq', 'earn']
    with open(probability, 'r') as prob:
        lines = prob.readlines()
        article_probability = [float(num) for num in lines[0].strip().split()]
        for line in lines[1:]:
            parts = line.split()
            key = parts[0]
            probs = [float(x) for x in parts[1:6]]
            word_prob[key] = probs
    article_classify={}
    print(article_probability)
    with open(testset, 'r') as file:
        raw_test_file = json.load(file)
        for article in raw_test_file:
            article_prior_prob = [0,0,0,0,0]
            for i in range(5):
                article_prior_prob[i]=math.log(article_probability[i])
            for word in article[2]:
                if word not in word_prob:
                    continue
                for i in range(5):
                    article_prior_prob[i] = article_prior_prob[i]+math.log(word_prob[word][i])
            max_index = article_prior_prob.index(max(article_prior_prob))
            article_classify[article[0]]=(categories[max_index])
    with open(outputfile, 'w') as f:
        for key, value in article_classify.items():
            f.write(key + ' ' + value + '\n')
    return


def f1_score(testset, classification_result):
    # TODO: Use the F_1 score to assess the performance of the implemented classification model
    #   The return value should be a float object.
    categories = ['crude', 'grain', 'money-fx', 'acq', 'earn']
    classification=[]
    test_set={}
    tpfpfn=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    f1=[0,0,0,0,0]
    with open(testset, 'r') as file:
        data = json.load(file)
        for item in data:
            id = ""
            for char in item[0]:
                if char.isdigit():
                    id += char
            test_set[id] = item[1]
    with open(classification_result, 'r') as file:
        for line in file:
            classification.append(line.strip().split())
    for classified_article in classification:
        for i in range(5):
            if classified_article[1]==categories[i]:
                if categories[i]==test_set[classified_article[0]]:
                    tpfpfn[i][0]+=1
                else:
                    tpfpfn[i][1]+=1
            else:
                if categories[i]==test_set[classified_article[0]]:
                    tpfpfn[i][2]+=1
    for i in range(5):
        p=tpfpfn[i][0]/(tpfpfn[i][0]+tpfpfn[i][1])
        r=tpfpfn[i][0]/(tpfpfn[i][0]+tpfpfn[i][2])
        f1[i]=2*p*r/(p+r)
    average_f1= sum(f1)/len(f1)
    return  average_f1


def main():
    ''' Main Function '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-pps', '--preprocess', type=str,
                        nargs=2, help='preprocess the dataset')
    parser.add_argument('-cw', '--count_word', type=str,
                        nargs=2, help='count the words from the corpus')
    parser.add_argument('-fs', '--feature_selection', type=str,
                        nargs=3, help='\select the features from the corpus')
    parser.add_argument('-cp', '--calculate_probability', type=str, nargs=3,
                        help='calculate the posterior probability of each feature word, and the prior probability of the class')
    parser.add_argument('-cl', '--classify', type=str, nargs=3,
                        help='classify the testset documents based on the probability calculated')
    parser.add_argument('-f1', '--f1_score', type=str, nargs=2,
                        help='calculate the F-1 score based on the classification result.')
    opt = parser.parse_args()

    if (opt.preprocess):
        input_file = opt.preprocess[0]
        output_file = opt.preprocess[1]
        preprocess(input_file, output_file)
    elif (opt.count_word):
        input_file = opt.count_word[0]
        output_file = opt.count_word[1]
        count_word(input_file, output_file)
    elif (opt.feature_selection):
        input_file = opt.feature_selection[0]
        threshold = int(opt.feature_selection[1])
        outputfile = opt.feature_selection[2]
        feature_selection(input_file, threshold, outputfile)
    elif (opt.calculate_probability):
        word_count = opt.calculate_probability[0]
        word_dict = opt.calculate_probability[1]
        output_file = opt.calculate_probability[2]
        calculate_probability(word_count, word_dict, output_file)
    elif (opt.classify):
        probability = opt.classify[0]
        testset = opt.classify[1]
        outputfile = opt.classify[2]
        classify(probability, testset, outputfile)
    elif (opt.f1_score):
        testset = opt.f1_score[0]
        classification_result = opt.f1_score[1]
        f1 = f1_score(testset, classification_result)
        print('The F1 score of the classification result is: '+str(f1))


if __name__ == '__main__':
    import os
    main()
