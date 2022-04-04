import linecache

def getline1 (num):
    return (linecache.getline('C:\\search_cw\\song_c11.csv',num))

def getline2 (num):
    return (linecache.getline('C:\\search_cw\\art7.csv',num))



def search_song (songN):
    f2=open('C:\\search_cw\\song_result.csv','w+',encoding='utf-8')
    n=1
    pointer_s=0
    limit_s=0
    while n<114396:
        sline=getline1(n)
        sline=sline[:-1]
        slist=sline.split(',')
        #print(songN)
        #print(slist[1])
        if songN == slist[1]:
            #print('**************\n')
            pointer_s=int(slist[0])
            line_s=getline2(pointer_s)
            list_s=line_s.split(',')
            f2.write(list_s[0])
            f2.write(',')
            f2.write(list_s[1])
            f2.write(',')
            f2.write(list_s[2])
            f2.write(',')
            f2.write('www.vagalume.com.br'+list_s[3])
            if limit_s==100:
                break
            limit_s+=1  
        #print(sline)
        n+=1
    f2.close()
    return None
