import linecache
import collections
import math
import operator

def preprocess_stem (tokenW):
 import nltk
 from nltk.stem import PorterStemmer
 ps=PorterStemmer()
 return ps.stem(tokenW)

def getline1 (num):
    return (linecache.getline('C:\\search_cw\\querymatch.csv',num))

def getline2 (num):
    return (linecache.getline('C:\\search_cw\\queryweight.csv',num))

def getline3 (num):
    return (linecache.getline('C:\\search_cw\\ceshistem2.csv',num))

def getline4 (num):
    return (linecache.getline('C:\\search_cw\\findlyc.csv',num))

f2=open('C:\\search_cw\\lyc_result.csv','a',encoding='utf-8')

#for query idf process
f1=open('C:\\search_cw\\idft_list111.csv','r',encoding='utf-8')
df_list=f1.readlines()


print('type in search content\n')
content=input()


#process query data: normalization; stemming; removing number and punctuation
newcontent=''
for line_char in content:
    if line_char==' 'or str.isalpha(line_char):
        newcontent+=line_char
    else:
        line_char=''
lycris=str.lower(newcontent)
lyc_list=lycris.split(' ')
list_temp=[]
for or_word in lyc_list:
    if or_word!='':
        new_word=preprocess_stem(or_word)
        list_temp.append(new_word)
lyc_list=list_temp
lyc_size=len(lyc_list)

#process query: tf, idf, weight
lyc_dic=collections.Counter(lyc_list)


for key in lyc_dic:
    for df_line in df_list:
        df_li_list=df_line.split(',')
        if key == df_li_list[0]:
            lyc_dic[key]='%.4f'%((1+math.log10(lyc_dic[key]))*float(df_li_list[1]))
f1.close()
print(lyc_dic)

lyc_list=list(lyc_dic.keys())

#print(lyc_list)

#process query->doc: 1.match 2.calculate cos 3.sort
doc_dic={}#{match doc: []list of all query words' weight values}//the order is match with (the keys in lyc_dic) and lyc_list
doc_lyc={}#{match doc: minimum tf word(queried) in that doc}
n1=1
while n1<114396:
    line1=getline1(n1)
    line1=line1[:-1]
    list1=line1.split(',')
    num1=int(list1[0])
    mark=0
    for lyc_word in lyc_list:
        #word=preprocess_stem(lyc_word)
        if lyc_word in list1:
            mark=1
        else:
            mark=0
            break
    if mark==1:
        line2=getline2(num1)
        list2=line2.split(',')
        doc_li_temp=[]
        index_temp=0
        for lyc_word in lyc_list:
            #print(lyc_word)#for test order of lyc_list and lyc_dic
            index_temp=list1.index(lyc_word)
            doc_li_temp.append(index_temp)
            doc_dic.setdefault(num1,[]).append(list2[index_temp])
        doc_lyc[num1]=list1[min(doc_li_temp)]
        #lyc_mat.append(num1)
    #lyc_mat.append(num1) if mark==1 else pass
    n1+=1
#print(doc_dic)
#print(doc_lyc)


#2.calculate cos
doc_cap={}
ab=0.0#product of query vector and doc vector// a: query; b: doc
ab_a=0.0
ab_b=0.0#for doc
aa=0.0
bb=0.0#length of doc
lyc_wei=[]#list of query word weight in order(the same sequent of lyc_dic && lyc_list)
#print('shang: doc\nxia: query\n')
for query_w_num in range(len(lyc_list)):
    #print(lyc_list[query_w_num])#for test order of lyc_list and lyc_dic
    lyc_wei.append(float(lyc_dic[lyc_list[query_w_num]]))
    aa+=lyc_wei[query_w_num]**2
aa=aa**0.5#aa= length of query

for key2 in doc_dic:# key is the same meaning with before: the index of matched doc
    for query_word_loc in range(len(lyc_list)):
        ab_b=float(doc_dic[key2][query_word_loc])
        ab_a=lyc_wei[query_word_loc]
        #ab+=ab_b*lyc_dic[lyc_list[query_word_loc]]
        ab+=ab_a*ab_b
        bb+=ab_b**2
    bb=bb**0.5
    ab='%.4f'%(ab/(aa*bb))
    doc_cap[key2]=ab
    ab=0.0
    ab_b=0.0
    bb=0.0
    ab_a=0.0

print(doc_cap)
print('\n******\n')
doc_cap=sorted(doc_cap.items(), key=lambda x:x[1], reverse=True)
doc_cap=dict(doc_cap)
print(doc_cap)

for key3 in doc_cap:
    line3=getline3(key3)
    line3=line3[:-1]
    list3=line3.split(' ')
    pointer=list3.index(doc_lyc[key3])
    if pointer<=4:
        pointer=4
    #elif: pointer>=(len(list3)-2):
    #    pointer=
    line4=getline4(key3)
    list4=line4.split(' ')
    #print(pointer)
    list4=list4[pointer-4:pointer+2]
    line4=' '.join(list4)
    print(key3)
    print(line4)

f2.close()


"""
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
"""
