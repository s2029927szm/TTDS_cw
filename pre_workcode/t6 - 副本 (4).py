"""
f2=open('C:\\search_cw\\idft_list111.csv','r',encoding='utf-8')
line=f2.readlines()
print (len(line))
f2.close()
"""

import linecache
import math
f2=open('C:\\search_cw\\weight444.csv','a',encoding='utf-8')
def getline1 (num):
    return (linecache.getline('C:\\search_cw\\tfnew44.csv',num))
    
def getidft (word):
    idft=0.0
    f1=open('C:\\search_cw\\idft_list44.csv','r',encoding='utf-8')
    df_list=f1.readlines()
    for df_str in df_list:
        df_s_list=df_str.split(',')
        if word == df_s_list[0]:
            idft=float(df_s_list[1])
            break
    if idft==0.0:
        print(word)
        print('idft word error')
    f1.close()
    return (idft)
     
            
n=112250
while n<114396:#114396
    line1=getline1(n)
    line1=line1[:-1]
    list1=line1.split(',')
    Itecount=len(list1)
    if n!= int(list1[0]):
        print("error***")
        break
    f2.write(str(n))
    k=1
    while k<Itecount:
        target=list1[k]
        tf1_ta=int(list1[k+1])
        idf=getidft(target)
        weight=(1+math.log10(tf1_ta))*idf
        f2.write(',')
        f2.write(target)
        f2.write(',')
        f2.write(str(weight))
        k+=2
    print(n)
    n+=1
    f2.write('\n')     
        
"""       
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
"""
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
