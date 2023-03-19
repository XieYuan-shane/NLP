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
if __name__ == '__main__':
    preprocess("train.json","train2.json")