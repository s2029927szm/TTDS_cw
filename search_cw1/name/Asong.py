def Asong1 (Num2):
    import linecache
    def getline1 (num):
        return (linecache.getline('C:\\search_cw\\name\\song_c.csv',num))
    """    
    n=1
    #Link=''
    while n<114396:
        asong=getline1(n)
        alist=asong.split(',')
        #print(slink)
        asong_n=int(alist[0])
        if Num2 ==slink_n:
            Songa=''.join(slink[1])
            break
        #print(sline)
        n+=1
        
    Songa=Songa[:-1]
    """
    
    k=0
    songs=''
    
    while k<3:
        asong=getline1(Num2)
        alist=asong.split(',')
        asong_n=int(alist[0])
        #print(asong_n)
        #print(Num2)
        Songa=''.join(alist[1])
        songs=songs+Songa
        k+=1
        Num2+=1
    
    songs=songs[:-1]
    
    
    return(songs)

#k=Asong(1000)
#print(k)
