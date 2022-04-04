def Ssong (songN):
    import linecache
    def getline1 (num):
        return (linecache.getline('C:\\search_cw\\name\\song_c.csv',num))
        
    n=0
    Snum=0
    while n<114396:
        sline=getline1(n)
        if songN in sline:
            slist=sline.split(',')
            Snum=int(slist[0])
            break
        #print(sline)
        n+=1
    return(Snum)


Ssong('A Campfire Song')
