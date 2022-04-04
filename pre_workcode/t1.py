f=open('C:\\search_cw\\lyrics_data1.csv','r',encoding='gb18030',errors='ignore')
f2=open('C:\\search_cw\\lyrics_data2.csv','a',encoding='gb18030')

count=1

while True:
    newline=''
    line_data=f.readline()
    if line_data.endswith('666aaa,',0,7):
        line_data=line_data[7:]
        for line_char in line_data:
            if line_char==' 'or str.isalpha(line_char):
                newline+=line_char
            else:
                line_char=''
        newline=str.lower(newline)
        f2.write(str(count))
        f2.write(',')
        f2.write(newline)
        f2.write('\n')
        count+=1
    
    elif line_data.endswith('666bbb,',0,7):
        break
    
    else:
        for line_char in line_data:
            if line_char==' 'or str.isalpha(line_char):
                newline+=line_char
            else:
                line_char=''
        newline=str.lower(newline)
        f2.write(newline)

f.close()
f2.close()


"""
a=f.readlines()
f.close()
print(a)
b=''.join(a)
f2=open('C:\\aTTDS\\a22.txt','a')
f2.write(b)
f2.close()
"""
