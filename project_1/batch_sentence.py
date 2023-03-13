import sentence
def batch_sentence(x, y):
    with open(x,'r',encoding = 'UTF-8') as f:
        with open(y, 'a',encoding = 'UTF-8') as output:
            lines = f.readlines()#rendlines()读取全部行，每行都转化为列表中的一项
            for line in lines:
                word = line.split()
                if(word[0] == 'R'):
                    str1 = []
                    for i in range(1,len(word)):
                        str1.append(word[i])
                    print(str1)
                    output.write(line)
                    continue
                elif(word[0] == 'H'):
                    str2 = []
                    for i in range(1, len(word)):
                        str2.append(word[i])
                    print(str1)
                    print(str2)
                    a,b = sentence.sentence_edit_distance(str1,str2)
                    print(a)
                    del str1[0]
                    output.write("{} {} \n".format(line.rstrip(),a))
    f.close()
    output.close()
batch_sentence('sentence_test','sentence_output')