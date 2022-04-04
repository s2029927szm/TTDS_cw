def sear_artist (artistN):
    import linecache
    def getline1 (num):
        return (linecache.getline('C:\\search_cw\\name\\artist_c.csv',num))
        
    n=0
    Snum1=0
    while n<1289:
        sline=getline1(n)
        if artistN in sline:
            slist=sline.split(',')
            Snum1=int(slist[0])
            break
        #print(sline)
        n+=1
    return(Snum1)


