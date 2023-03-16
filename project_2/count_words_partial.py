import json
from collections import Counter #Counter方法可以实现字典相加
def count_word(inputfile,outputfile):
    #TODO: count the words from the corpus, and output the result to the output file in the format required.
    #   A dictionary object may help you with this work.
    with open(inputfile,'r') as input:
        file_contents = json.load(input) 
        crude_count = {}
        all1 = 0
        grain_count = {}
        all2 = 0
        money_count = {}
        all3 = 0
        acq_count = {}
        all4 = 0
        earn_count = {}
        all5 = 0
        for i in range(0, len(file_contents)):
            if file_contents[i][1] == 'crude':
                for crude_key in file_contents[i][2]:
                        crude_count[crude_key] = crude_count.get(crude_key, 0) + 1
                        all1 = all1 + 1
            if file_contents[i][1] == 'grain':
                for grain_key in file_contents[i][2]:
                        grain_count[grain_key] = grain_count.get(grain_key, 0) + 1
                        all2 = all2 + 1
            if file_contents[i][1] == 'money-fx':
                for money_key in file_contents[i][2]:
                        money_count[money_key] = money_count.get(money_key, 0) + 1
                        all3 = all3 + 1
            if file_contents[i][1] == 'acq':
                for acq_key in file_contents[i][2]:
                        acq_count[acq_key] = acq_count.get(acq_key, 0) + 1
                        all4 = all4 + 1
            if file_contents[i][1] == 'earn':
                for earn_key in file_contents[i][2]:
                        earn_count[earn_key] = earn_count.get(earn_key, 0) + 1 
                        all5 = all5 + 1   
        all_count = dict(Counter(crude_count)+Counter(grain_count)+Counter(money_count)+Counter(acq_count)+Counter(earn_count))         
        with open(outputfile, 'a') as output:
            output.write("Word_count.txt:\n")
            output.write("{} {} {} {} {}\n".format(all1,all2,all3,all4,all5))
            for j in all_count.keys():
                output.write("{} {} {} {} {} {}\n".format(j,crude_count.get(j, 0),grain_count.get(j, 0),money_count.get(j, 0),
                                                    acq_count.get(j, 0),earn_count.get(j, 0)) )   
    input.close()
    output.close()
    return
count_word('train_test.json','word_count.txt')