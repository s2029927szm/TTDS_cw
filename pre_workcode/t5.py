import linecache
#import math
f2=open('C:\\search_cw\\tfnew11.csv','a',encoding='utf-8')
def getline1 (num):
    return (linecache.getline('C:\\search_cw\\tf222.csv',num))
    
dic={}
n=1
while n<114396:
    line1=getline1(n)
    line1=line1.split(",,1")[0]
    f2.write(line1)
    f2.write('\n')
    n+=1

f2.close()
