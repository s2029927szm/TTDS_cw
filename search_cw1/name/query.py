import song
import link
import artist
import Sartist
import Asong

A_link=''
A_songs=[]
S_link=''
S_artist=''



#111 search artist
def queryA (qterm1):
    qterm1=str.lower(qterm1)
    num=Sartist.sear_artist(qterm1)
    A_songs.append(Asong.Asong1(num))
    return None

#222 search song
def queryS (qterm):
    #qterm='A Campfire Song'

    qterm=str.lower(qterm)
    num=song.Ssong(qterm)#search song
    S_link=link.Slink(num)#get link
    S_artist=artist.Songartist(num)#get artist
    
    #print(num)
    #print(a)
    #print(b)
    
    return None

print('type in search model:\n')
model=input()
print('type in search content\n')
content=input()

if model=='111':
    queryA(content)
elif model=='222':
    queryS(content)
elif model=='333':
    queryL(content)
else:
    print('wrong model')


print(''.join(A_songs))
