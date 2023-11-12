# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:06:28 2023

@author: Zhao Li
# @File: Knowledge Hypergraph Data Processing
"""

import os
os.getcwd()

# new_path = '/your/new/directory/path'
# os.chdir(new_path)


### n-ary dataset generation ###

ary_2 = []
ary_3 = []
ary_4 = []
ary_5 = []
ary_6 = []
ary_7 = []
ary_8 = []
ary_9 = []

## train dataset
with open("./train.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split("\t")
        rel = line[0]
        ents = line[1:]
        if len(ents) == 2:
            ary_2.append([rel] + ents)
        elif len(ents) == 3:
            ary_3.append([rel] + ents)
        elif len(ents) == 4:
            ary_4.append([rel] + ents)
        elif len(ents) == 5:
            ary_5.append([rel] + ents)
        elif len(ents) == 6:
            ary_6.append([rel] + ents)
        elif len(ents) == 7:
            ary_7.append([rel] + ents)
        elif len(ents) == 8:
            ary_8.append([rel] + ents)    
        elif len(ents) == 9:
            ary_9.append([rel] + ents)
    f.close()

for i in [2, 3, 4, 5, 6, 7, 8, 9]:
    with open("./train_{}.txt".format(i), "w") as f:
        for tuple_ in eval("ary_{}".format(i)):
            for k in range(len(tuple_)):
                if k != len(tuple_) - 1:
                    f.write(tuple_[k])
                    f.write("\t")
                else:
                    f.write(tuple_[k])
            f.write("\n")
        f.close()



## test dataset

ary_2 = []
ary_3 = []
ary_4 = []
ary_5 = []
ary_6 = []
ary_7 = []
ary_8 = []
ary_9 = []

with open("./test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split("\t")
        rel = line[0]
        ents = line[1:]
        if len(ents) == 2:
            ary_2.append([rel] + ents)
        elif len(ents) == 3:
            ary_3.append([rel] + ents)
        elif len(ents) == 4:
            ary_4.append([rel] + ents)
        elif len(ents) == 5:
            ary_5.append([rel] + ents)
        elif len(ents) == 6:
            ary_6.append([rel] + ents)
        elif len(ents) == 7:
            ary_7.append([rel] + ents)
        elif len(ents) == 8:
            ary_8.append([rel] + ents)    
        elif len(ents) == 9:
            ary_9.append([rel] + ents)
    f.close()

for i in [2, 3, 4, 5, 6, 7, 8, 9]:
    with open("./test_{}.txt".format(i), "w") as f:
        for tuple_ in eval("ary_{}".format(i)):
            for k in range(len(tuple_)):
                if k != len(tuple_) - 1:
                    f.write(tuple_[k])
                    f.write("\t")
                else:
                    f.write(tuple_[k])
            f.write("\n")
        f.close()



## valid dataset

ary_2 = []
ary_3 = []
ary_4 = []
ary_5 = []
ary_6 = []
ary_7 = []
ary_8 = []
ary_9 = []

with open("./valid.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split("\t")
        rel = line[0]
        ents = line[1:]
        if len(ents) == 2:
            ary_2.append([rel] + ents)
        elif len(ents) == 3:
            ary_3.append([rel] + ents)
        elif len(ents) == 4:
            ary_4.append([rel] + ents)
        elif len(ents) == 5:
            ary_5.append([rel] + ents)
        elif len(ents) == 6:
            ary_6.append([rel] + ents)
        elif len(ents) == 7:
            ary_7.append([rel] + ents)
        elif len(ents) == 8:
            ary_8.append([rel] + ents)    
        elif len(ents) == 9:
            ary_9.append([rel] + ents)
    f.close()

for i in [2, 3, 4, 5, 6, 7, 8, 9]:
    with open("./valid_{}.txt".format(i), "w") as f:
        for tuple_ in eval("ary_{}".format(i)):
            for k in range(len(tuple_)):
                if k != len(tuple_) - 1:
                    f.write(tuple_[k])
                    f.write("\t")
                else:
                    f.write(tuple_[k])
            f.write("\n")
        f.close()