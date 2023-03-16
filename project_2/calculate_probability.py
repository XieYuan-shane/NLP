def calculate_probability(word_dict,word_count,outputfile):
    #TODO: Calculate the posterior probability of each feature word, and the prior probability of the class.
    #   Output the result to the output file in the format required
    #   Use 'word_count.txt' and ‘word_dict.txt’ jointly.
    with open(word_dict,'r') as input:
        with open(outputfile,'w') as output:
            output.write("word_probability.txt:\n")
            input.readline()
            line1 = input.readline()
            line1 = line1.replace("\n", '') #去除每一行末尾的换行符
            x = line1.split(' ')
            for i in range(0,5):
                x[i] = int(x[i])#拆分文本出来的是字符，要转为整型  
            all = x[0] + x[1] + x[2] + x[3] + x[4]
            output.write("{} {} {} {} {}\n".format(x[0]/all, x[1]/all, x[2]/all, x[3]/all, x[4]/all))
            while True:
                line_other = input.readline()
                if line_other:
                    line_other = line_other.replace("\n", '') #去除每一行末尾的换行符
                    y = line_other.split(' ')
                    for i in range(1,6):
                       y[i] = int(y[i])#拆分文本出来的是字符，要转为整型
                    #在这里add1 smooth
                    output.write("{} {} {} {} {} {}\n".format(y[0], (y[1]+1)/(x[0]+10000), (y[2]+1)/(x[1]+10000), 
                                                                (y[3]+1)/(x[2]+10000), (y[4]+1)/(x[3]+10000),(y[5]+1)/(x[4]+10000)))
                else:
                    break
    input.close()
    output.close()
    return
if __name__ == '__main__':
    calculate_probability('word_dict.txt','word_count','word_probability.txt')