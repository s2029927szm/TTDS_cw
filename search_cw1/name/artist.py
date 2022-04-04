def Songartist (Numa):
    import linecache
    def getline1 (num):
        return (linecache.getline('C:\\search_cw\\name\\artist_c.csv',num))
        
    n=1
    #Link=''
    while n<1289:#1289list
        soartist=getline1(n)
        soartist=soartist.split(',')
        #print(slink)
        soartist_n1=int(soartist[0])
        soartist_n2=int(soartist[1])
        if Numa >=soartist_n1 and Numa<=soartist_n2:
            Artist=''.join(soartist[2])
            break
        #print(sline)
        n+=1
    return(Artist)
