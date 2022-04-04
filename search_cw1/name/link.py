def Slink (Numl):
    import linecache
    def getline1 (num):
        return (linecache.getline('C:\\search_cw\\name\\link_c.csv',num))
        
    n=1
    #Link=''
    while n<114396:
        slink=getline1(n)
        slink=slink.split(',')
        #print(slink)
        slink_n=int(slink[0])
        if Numl ==slink_n:
            Link=''.join(slink[1])
            break
        #print(sline)
        n+=1
    Link=Link[:-1]
    return(Link)
