import linecache
import math
f2=open('C:\\search_cw\\tf222.csv','a',encoding='utf-8')
def getline1 (num):
    return (linecache.getline('C:\\search_cw\\ceshistem2.csv',num))
    
dic={}
n=1
while n<114396:
    line1=getline1(n)
    line1=line1[:-1]
    list1=line1.split(' ')
    for word in list1:
        if word not in dic:
            dic[word]=1
        else:
            dic[word]+=1
    f2.write(str(n))
    for term in dic:
        value1=dic.get(term)
        f2.write(',')
        f2.write(term)
        f2.write(',')
        f2.write(str(value1))
    n+=1
    f2.write('\n')
    dic.clear()

f2.close()

"""   
def preprocess_stem (tokenW):
 import nltk
 from nltk.stem import PorterStemmer
 ps=PorterStemmer()
 return ps.stem(tokenW)

n=0
while n<114395:
    #line=getline1(n)
    line=f.readline()
    list=line.split()
    for word in list:
        word=preprocess_stem(word)
        f2.write(word)
        f2.write(' ')
    f2.write('\n')
    print(n)
    n+=1
f2.close()
"""
