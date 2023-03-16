import json
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
if __name__ == '__main__':
    classify('word_probability.txt','test_test.json','classification_result.txt')