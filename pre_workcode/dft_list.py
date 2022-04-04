import math
import linecache
f2=open('C:\\search_cw\\idft_ceshi.csv','a',encoding='gb18030')
def getline1 (num):
    return (linecache.getline('C:\\search_cw\\ceshistem1.csv',num))



list1=[]

def pretermlist ():
    n=0
    while n<114395:
        #line1=f.readline()
        line1=getline1(n)
        line1=line1[0:-1]
        list3=line1.split()
        list1.extend(list3)
        n+=1
    #f.close()
    return None

def count_dft (w1):
    #f1=open('C:\\search_cw\\lyrics_data3.csv','r',encoding='gb18030',errors='ignore')
    n1=0
    count1=0
    while n1<114395:
        #line1=f1.readline()
        line1=getline1(n1)
        if word in line1:
            count1+=1
        n1+=1
    return count1

pretermlist ()
list1=list(set(list1))
print(len(list1))



for word in list1:
    dft=0
    if len(word)<13 and word.count(max(word,key=word.count))<3:
        dft=count_dft(word)
        dft=114395/dft
        dft=math.log10(dft)
    else:
        dft=114395/1
        dft=math.log10(dft)
    f2.write(word)
    f2.write(',')
    f2.write(str(dft))
    f2.write('\n')
    print(word)

f2.close()





"""
import math
f1_dftl=open('C:\\search_cw\\lyrics_data3_1.csv','r',encoding='gb18030',errors='ignore')
f2_dftl=open('C:\\search_cw\\idft.csv','a',encoding='gb18030')

list2=[]
list3=[]
list4=[]
def pretermlist ():
    n=209203
    while n:
        line1=f1_dftl.readline()
        line1=line1[0:-1]
        list3=line1.split()
        list2.extend(list3)
        n-=1
        #print(n)
    return None
pretermlist()

list2=list(set(list2))
print(len(list2))


f1_dftl.close()
f2_dftl.close()

    line1=f1_dftl.readline()
    list2=line1.split()
    for term1 in list2:
        if term1 not in list1:
            list1.append(term1)
    f.close()
    return None

def count_dft (w1):
    f1=open('C:\\search_cw\\lyrics_data3.csv','r',encoding='gb18030',errors='ignore')
    n1=209203
    count1=0
    while n1:
        line1=f1.readline()
        if word in line1:
            count1+=1
        n1-=1
    f1.close()
    return count1


pretermlist ()


dft=0
f2.close()


for word in list1:
    dft=count_dft(word)
    dft=209203/dft
    dft=math.log10(dft)
    f2.write(word)
    f2.write(',')
    f2.write(str(dft))
    f2.write('\n')
    print(word)

f2.close()
"""


"""
line1=f.readline()
dic1={}
xx=209206

while xx:
    line1=f.readline()
    list1=line1.split()
    for word1 in list1:
        if word1 not in dic1:
            dic1[word1]=1
        else:
            dic1[word1]+=1
            word1=''   
    xx-=1

for term in doc


"""




"""
a=f.readlines()
f.close()
print(a)
b=''.join(a)
f2=open('C:\\aTTDS\\a22.txt','a')
f2.write(b)
f2.close()
"""
