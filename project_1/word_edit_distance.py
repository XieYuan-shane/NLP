import numpy as np

def min_edit_distance(str1, str2):

    str1 = '#' + str1
    str2 = '#' + str2
    print(str1)
    len1 = len(str1)
    len2 = len(str2)
    #记录开销的矩阵
    solutionmatrix = np.zeros((len2, len1))

    #初始化
    for i in range(0, len1):
        solutionmatrix[0][i] = i
    for i in range(0, len2):
        solutionmatrix[i][0] = i

    #记录路径的矩阵,并初始化之前初始化的路径
    #数字3表示添加，数字4表示删除

    recordmatrix1 = np.zeros((len2, len1))
    for i in range(0, len1):
        recordmatrix1[0][i] = 3
    for i in range(0, len2):
        recordmatrix1[i][0] = 4
    recordmatrix1[0][0] = 100  #回溯终止符

    #判断两个字符串当前位置是否相等
    cost = 0
    for i in range(1, len2):
        for j in range(1, len1):
            if str1[j] == str2[i]:
                cost = 0
            else:
                cost = 2

            #计算开销
            substitute = solutionmatrix[i - 1][j - 1] + cost
            insert = solutionmatrix[i][j - 1] + 1
            delete = solutionmatrix[i-1][j] +1
            solutionmatrix[i][j] = min(substitute, insert, delete)

            #记录路径，操作的优先级不同，路径也不同，这里仅拿两种优先级举例
            prior1 = [substitute, insert, delete]     #替换优于添加
            whichone1 = prior1.index(min(prior1))

            #记录【i，j】是怎么变化而来的  2=替换，3=添加，4=删除，5=保留
            if whichone1 == 0 and cost == 2:
                recordmatrix1[i][j] = 2
            elif whichone1 == 0 and cost == 0:
                recordmatrix1[i][j] = 5
            elif whichone1 == 1:
                recordmatrix1[i][j] = 3
            else:
                recordmatrix1[i][j] = 4

    #回溯路径
    alignment = [[], []]
    i1 = len2-1
    j1 = len1-1
    temp1 = recordmatrix1[i1][j1]

    while temp1 != 100:
        if temp1 == 2:#2表示substitute
            alignment[1].append(str2[i1])
            alignment[0].append(str1[j1])
            i1 = i1-1
            j1 = j1-1

        elif temp1 == 5:#5表示保留
            alignment[1].append(str2[i1])
            alignment[0].append(str1[j1])
            i1 = i1 - 1
            j1 = j1 - 1

        elif temp1 == 3:#3表示添加
            alignment[1].append("{}".format(str1[j1]))
            alignment[0].append("{}".format('-'))
            j1 = j1-1

        elif temp1 ==4:
            alignment[1].append("{}".format('-'))
            alignment[0].append("{}".format(str2[i1]))
            i1 = i1-1

        temp1 = recordmatrix1[i1][j1]

    alignment[0].reverse()
    alignment[1].reverse()

    min_distance = int(solutionmatrix[len2-1][len1-1])
    return min_distance,alignment

if __name__ == '__main__':
    str1 = input("请输入str1： ")
    str2 = input("请输入str2： ")
    min_edit_distance(str2, str1)