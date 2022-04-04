import linecache

def getline1 (num):
    return (linecache.getline('C:\\search_cw\\art3.csv',num))

def getline2 (num):
    return (linecache.getline('C:\\search_cw\\art7.csv',num))

def search_art (artistN):
    f2=open('C:\\search_cw\\art_result.csv','w+',encoding='utf-8')
    n=1
    start_a=1
    end_a=1
    limit_a=0
    while n<1289:
        sline=getline1(n)
        if artistN in sline:
            slist=sline.split(',')
            start_a=int(slist[0])
            end_a=int(slist[1])+1
            break
        #print(sline)
        n+=1
     
    while start_a < end_a:
        line_a=getline2(start_a)
        list_a=line_a.split(',')
        f2.write(list_a[0])
        f2.write(',')
        f2.write(list_a[1])
        f2.write(',')
        f2.write(list_a[2])
        f2.write(',')
        f2.write('www.vagalume.com.br'+list_a[3])
        start_a+=1
        if limit_a==100:
            break
        limit_a+=1
    f2.close()        
    return None


