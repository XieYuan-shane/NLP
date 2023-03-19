import json
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
        F1 = [0,0,0,0,0]
        for i in range(5):
            P[i] = TP[i]/(TP[i]+FP[i])
            R[i] = TP[i]/(TP[i]+FN[i])
        P_ave = (P[0]+P[1]+P[2]+P[3]+P[4])/5
        R_ave = (R[0]+R[1]+R[2]+R[3]+R[4])/5
        F1 = (2*P_ave*R_ave)/(P_ave+R_ave)
        
    return F1
if __name__ == '__main__':
    F1 = f1_score('test.preprocessed.json','classification_result.txt')
    print(F1)