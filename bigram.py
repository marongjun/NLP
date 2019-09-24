#Bigram Model
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.util import ngrams
import re

# Function to generate n-grams from sentences.
def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

ngramN_2 = []
ngramP_2 = []
ngramN_1 = []
ngramP_1 = []

#read 0-299 N train data 
for i in range (0,300):
    with open("movies/train/N-train"+str(i)+".txt") as f:
        data_pre = f.read() 
        data_lower = data_pre.lower()              #clean data, all to lower cases
        Sent_tokens = sent_tokenize(data_lower)
        for x in Sent_tokens:
            data = re.sub(r"[^a-zA-Z0-9]",' ',x)   #clean data, remove all punctuations
            ngramN_2.append(extract_ngrams(data, 2))
            ngramN_1.append(extract_ngrams(data, 1))
#print(ngramN_2) 

#read 300-599 P train data 
for i in range (300,600):
    with open("movies/train/P-train"+str(i)+".txt") as f:
        data_pre = f.read() 
        data_lower = data_pre.lower() 
        Sent_tokens = sent_tokenize(data_lower)    #clean data, all to lower cases
        for x in Sent_tokens:
            data = re.sub(r"[^a-zA-Z0-9]",' ',x)   #clean data, remove all punctuations
            ngramP_2.append(extract_ngrams(data, 2))
            ngramP_1.append(extract_ngrams(data, 1))
#print(ngramP_2)
#print(ngramP_1)

#Dictionary key:word 2-gram   value:times

Dic_ngram2N = {}
Dic_ngram2P = {}

for ele in ngramN_2:
    for nwords in ele:
        if nwords not in Dic_ngram2N.keys():
            Dic_ngram2N[nwords] = 1
        else:
            Dic_ngram2N[nwords] += 1
#print(Dic_ngram2N)
            
for ele in ngramP_2:
    for nwords in ele:
        if nwords not in Dic_ngram2P.keys():
            Dic_ngram2P[nwords] = 1
        else:
            Dic_ngram2P[nwords] += 1
#print(Dic_ngram2P)

#Dictionary key:word 1-gram   value:times

Dic_ngram1N = {}
Dic_ngram1P = {}

for ele in ngramN_1:
    for nwords in ele:
        if nwords not in Dic_ngram1N.keys():
            Dic_ngram1N[nwords] = 1
        else:
            Dic_ngram1N[nwords] += 1
#print(Dic_ngram1N)
            
for ele in ngramP_1:
    for nwords in ele:
        if nwords not in Dic_ngram1P.keys():
            Dic_ngram1P[nwords] = 1
        else:
            Dic_ngram1P[nwords] += 1
#print(Dic_ngram2P)

#total number of words for 1-gram
Nneg1 = 0
Npos1 = 0 
for ele in Dic_ngram1N:
    Nneg1 += Dic_ngram1N[ele]

print(Nneg1)

for ele in Dic_ngram1P:
    Npos1 += Dic_ngram1P[ele]    
print(Npos1)

#Probablity of every word  frequency/total words with smoothing k=1  -- 1-gram
Prob_N1 = {}
Prob_P1 = {}

#Size of vocabulary
Vneg1 = len(Dic_ngram1N)
Vpos1 = len(Dic_ngram1P)
print(Vneg1)
print(Vpos1)

for ele in Dic_ngram1N:
    Prob_N1[ele] = (Dic_ngram1N[ele]+1)/(Nneg1+Vneg1)

#print(Prob_N1)

for ele in Dic_ngram1P:
    Prob_P1[ele] = (Dic_ngram1P[ele]+1)/(Npos1+Vpos1)  

#Dictionary key:word 1-gram   value:times

Dic_ngram1N = {}
Dic_ngram1P = {}

for ele in ngramN_1:
    for nwords in ele:
        if nwords not in Dic_ngram1N.keys():
            Dic_ngram1N[nwords] = 1
        else:
            Dic_ngram1N[nwords] += 1
#print(Dic_ngram1N)
            
for ele in ngramP_1:
    for nwords in ele:
        if nwords not in Dic_ngram1P.keys():
            Dic_ngram1P[nwords] = 1
        else:
            Dic_ngram1P[nwords] += 1
#print(Dic_ngram2P)

#total number of words for 1-gram
Nneg1 = 0
Npos1 = 0 
for ele in Dic_ngram1N:
    Nneg1 += Dic_ngram1N[ele]

print(Nneg1)

for ele in Dic_ngram1P:
    Npos1 += Dic_ngram1P[ele]    
print(Npos1)

#Probablity of every word  frequency/total words with smoothing k=1  -- 1-gram
Prob_N1 = {}
Prob_P1 = {}

#Size of vocabulary
Vneg1 = len(Dic_ngram1N)
Vpos1 = len(Dic_ngram1P)
print(Vneg1)
print(Vpos1)

for ele in Dic_ngram1N:
    Prob_N1[ele] = (Dic_ngram1N[ele]+1)/(Nneg1+Vneg1)

#print(Prob_N1)

for ele in Dic_ngram1P:
    Prob_P1[ele] = (Dic_ngram1P[ele]+1)/(Npos1+Vpos1)  

#Dictionary key:word 1-gram   value:times

Dic_ngram1N = {}
Dic_ngram1P = {}

for ele in ngramN_1:
    for nwords in ele:
        if nwords not in Dic_ngram1N.keys():
            Dic_ngram1N[nwords] = 1
        else:
            Dic_ngram1N[nwords] += 1
#print(Dic_ngram1N)
            
for ele in ngramP_1:
    for nwords in ele:
        if nwords not in Dic_ngram1P.keys():
            Dic_ngram1P[nwords] = 1
        else:
            Dic_ngram1P[nwords] += 1
#print(Dic_ngram2P)

#total number of words for 1-gram
Nneg1 = 0
Npos1 = 0 
for ele in Dic_ngram1N:
    Nneg1 += Dic_ngram1N[ele]

print(Nneg1)

for ele in Dic_ngram1P:
    Npos1 += Dic_ngram1P[ele]    
print(Npos1)

#Probablity of every word  frequency/total words with smoothing k=1  -- 1-gram
Prob_N1 = {}
Prob_P1 = {}

#Size of vocabulary
Vneg1 = len(Dic_ngram1N)
Vpos1 = len(Dic_ngram1P)
print(Vneg1)
print(Vpos1)

for ele in Dic_ngram1N:
    Prob_N1[ele] = (Dic_ngram1N[ele]+1)/(Nneg1+Vneg1)

#print(Prob_N1)

for ele in Dic_ngram1P:
    Prob_P1[ele] = (Dic_ngram1P[ele]+1)/(Npos1+Vpos1)  

#Run with the Test data
import numpy as np
test = {}

for i in range (0,50):
    if i <25:
        c = 'N'
    else:
        c = 'P'
    Dic_temp = {}  
    temp = []
    temp1 = []
    Ppos = 0
    Pneg = 0
    with open("movies/test/"+str(c)+"-test"+str(i)+".txt") as f:
        data_pre = f.read() 
        data_lower = data_pre.lower()
        Sent_tokens = sent_tokenize(data_lower)
        for x in Sent_tokens:
            data = re.sub(r"[^a-zA-Z0-9]",' ',x)
            temp.append(extract_ngrams(data, 2))
            temp1.append(extract_ngrams(data, 1))
        #print(temp1)
        for ele in temp1:
            if ele != []:
                #print (ele)
                first = ele[0]
                #print(first)
                if first in Prob_P1:
                    Ppos += np.log2(Prob_P1[first])       # calculate the first word probability
                for element in temp:
                 #print(element)
                  for word in element:
                        if word in Prob_P:
                            Ppos += np.log2(Prob_P[word])
        for ele in temp1:
            if ele != []:
                #print (ele)
                first = ele[0]
                #print(first)
                if first in Prob_N1:
                    Pneg += np.log2(Prob_N1[first])       # calculate the first word probability
                for element in temp:
#                 #print(element)
                  for word in element:
                      if word in Prob_N:
                          Pneg += np.log2(Prob_N[word])

                    
        #print (Ppos, Pneg)
        if Ppos < Pneg:
            test[i] = 'P'
        else:
            test[i] = 'N'
print(test)

#write txt - result of n-gram
file = open("movies/result_bi.txt","w+") 
for x in test:
    if x < 25:
        c = 'N'
    else:
        c = 'P'
    file.write(str(c)+"-test"+str(x)+" "+ str(test[x])+"\n")

file.close()