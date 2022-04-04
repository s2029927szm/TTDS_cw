import linecache
#import math
f1=open('C:\\search_cw\\weight1.csv','r',encoding='utf-8')
f2=open('C:\\search_cw\\querymatch.csv','a',encoding='utf-8')
f3=open('C:\\search_cw\\queryweight.csv','a',encoding='utf-8')
def getline1 (num):
    return (linecache.getline('C:\\search_cw\\tfnew11.csv',num))

n=1
while n<114396:#114396
    line1=getline1(n)
    line1=line1[:-1]
    list1=line1.split(',')
    
    line2=f1.readline()
    line2=line2[:-1]
    list2=line2.split(',')
    
    f2.write(str(n))
    f2.write(',')
    
    f3.write(str(n))
    f3.write(',')
    
    for i in range(2,len(list1),2):
        cpa=int(list1[2])
        count=2
        for W_index in range(2,len(list1),2):
            W_i=int(list1[W_index])
            if cpa<=W_i:
                pass
                #print(cpa,W_i)
            else:
                cpa=W_i
                count=W_index
                
        f2.write(list1[count-1])
        f2.write(',')
        
        f3.write(list2[count][:7])
        f3.write(',')

        list1[count]='99'
        #del list1[count-1:count]
        #del list2[count-1:count]
        #list1.remove(list1[count-1])
        #list1.remove(list1[count])
        #list2.remove(list1[count-1])
        #list2.remove(list2[count-1])
        
    f2.write('\n')
    f3.write('\n')
    n+=1
    print(n)

f1.close()
f2.close()
f3.close()

