f=open('C:\\search_cw\\name\\prework\\artist.csv','r',encoding='gb18030',errors='ignore')
f1=open('C:\\search_cw\\name\\prework\\artist_c.csv','a',encoding='utf-8')

n=0

start=0
end=0
count=1
term2='/10000-maniacs/'
aa='-'

while n<114396:
    line=f.readline()
    line=str.lower(line)
    line=line[:-1]#del \n
    
    list1=line.split(',')
    start=int(list1[0])
    termn=''.join(list1[1])
    if termn==term2:
        count+=1
    else:
        end=start-1
        start=end-count+1
        f1.write(str(start))
        f1.write(',')
        f1.write(str(end))
        f1.write(',')
        term2=term2[1:]
        term2=term2[:-1]
        term2=term2.replace('-',' ')
        f1.write(term2)
        f1.write('\n')
        term2=termn
        count=1
    n+=1
f.close()
f1.close()
