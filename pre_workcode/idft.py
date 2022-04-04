
import math
f2=open('C:\\search_cw\\idft.csv','a',encoding='gb18030')

list1=[]

def pretermlist ():
    f=open('C:\\search_cw\\lyrics_data3_1.csv','r',encoding='gb18030',errors='ignore')
    lines1=f.readlines()
    a=' '.join(lines1)
    list2=a.split()
    for term in list2:
        if term not in list1:
            list1.append(term)
            print(term)
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

"""
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
