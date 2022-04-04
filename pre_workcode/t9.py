f=open('C:\\search_cw\\lyrics_data33.csv','r',encoding='gb18030',errors='ignore')
f2=open('C:\\search_cw\\findlyc.csv','a',encoding='utf-8')

n=0
while n<114396:
    line=f.readline()
    f2.write(line)
    print(n)
    n+=1
f2.close()
f.close()
