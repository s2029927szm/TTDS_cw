import linecache
f=open('C:\\search_cw\\lyrics_data33.csv','r',encoding='gb18030',errors='ignore')
f2=open('C:\\search_cw\\ceshistem.csv','a',encoding='utf-8')
#def getline1 (num):
#    return (linecache.getline('C:\\search_cw\\lyrics_data33.csv',num,encoding='gb18030',errors='ignore'))

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
