import json
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer   # from nltk.stem import PorterStemmer
def preprocess(inputfile,outputfile):
    #TODO: preprocess the input file, and output the result to the output file: train.preprocessed.json,test.preprocessed.json
    #   Delete the useless symbols
    #   Convert all letters to the lowercase
    #   Use NLTK.word_tokenize() to tokenize the sentence
    #   Use nltk.PorterStemmer to stem the words
    with open(outputfile,'a') as output:
        with open(inputfile,'r') as input:
        #将json文件打开并转化为列表+字典
            file_contents = json.load(input) #对json文件中读取信息
            #  print(file_contents2[1][2])
            length = len(file_contents)
            tokenizer = RegexpTokenizer(r"[a-z]+(?:[-.'][a-z]+)?")#对字符以什么样的形式裁剪
            porter_stemmer = PorterStemmer()   # 词干提取
            #  print(length)
            #  因为是多重列表，这里进行lower（）
            for i in range(length):
                for j in range(len(file_contents[0])):
                    file_contents[i][j] = file_contents[i][j].lower() #全部化为小写
            #  这里进行数据处理
            for i in range(length):     
                file_contents[i][2] = tokenizer.tokenize(file_contents[i][2])#按照tokenizer定义的格式对列表进行分词
                for j in range(len(file_contents[i][2])):
                    file_contents[i][2][j] = porter_stemmer.stem(file_contents[i][2][j])
            json.dump(file_contents,output)#以json的格式写入文件中
    input.close()
    output.close()
    return
if __name__ == '__main__':
    preprocess('test.json','test_test.json')