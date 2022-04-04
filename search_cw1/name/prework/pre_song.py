f=open('C:\\search_cw\\name\\prework\\song.csv','r',encoding='gb18030',errors='ignore')
f1=open('C:\\search_cw\\name\\prework\\song_c.csv','a',encoding='utf-8')

n=0
while n<114396:
    line=f.readline()
    line=str.lower(line)
    f1.write(line)
    n+=1
f.close()
f1.close()
