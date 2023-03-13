#文件打开用open，写入用write。
#注意事项：文件读取一行，不是单独读取字符串，后面的空白也会被读取，因此需要rstrip（）去除空白


import word_edit_distance
def batch_word(x, y):
    with open(x,'r') as f:
        with open(y, 'a') as output:
            lines = f.readlines()
            for line in lines:
                word = line.split()
                if(word[0] == 'R'):
                    str1 = word[1]
                    output.write(line)
                    continue

                elif(word[0] == 'H'):
                    str2 = word[1]
                    distance = str(word_edit_distance.min_edit_distance(str1,str2))
                    output.write("{} {} \n".format(line.rstrip(),distance[1]))
    f.close()
    output.close()
batch_word('word_test','word_output')