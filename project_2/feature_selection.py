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
if __name__ == '__main__':
     feature_selection('word_count.txt',10000,'word_dict.txt')