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




file = ["train_8.txt", "test_8.txt", "valid_8.txt"]
id2ent = {}
ent2id = {}
rel2id = {}
i = 0
j = 0
for filename in file:
    with open("./{}".format(filename)) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split("\t")
            rel = line[0]
            if rel not in rel2id:
                rel2id[rel] = j
                j += 1
            ents = line[1:]
            for ent in ents:
                if ent not in ent2id:
                    ent2id[ent] = i
                    i+=1

with open("entities.dict", "w") as f:
    for key, value in ent2id.items():
        f.write(str(value)+"\t"+key+"\n")

with open("relations.dict", "w") as f:
    for key, value in rel2id.items():
        f.write(str(value)+"\t"+key+"\n")
        


with open("entities.txt", "w") as f:
    for key, value in ent2id.items():
        f.write(str(value)+"\t"+key+"\n")

with open("relations.txt", "w") as f:
    for key, value in rel2id.items():
        f.write(str(value)+"\t"+key+"\n")



print(len(ent2id))
print(len(rel2id))