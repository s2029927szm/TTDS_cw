f=open('C:\\search_cw\\name\\artist.csv','r',encoding='gb18030',errors='ignore')
f1=open('C:\\search_cw\\name\\artist_c_normal.csv','a',encoding='utf-8')

n=0
while n<114396:
    line=f.readline()
    line=str.lower(line)
    list1=line.split(',')
    sort=''.join(list1[0])
    line=''.join(list1[1])
    line=line[1:]
    line=line[:-2]
    f1.write(sort)
    f1.write(',')
    f1.write(line)
    f1.write('\n')
    n+=1
f.close()
f1.close()
