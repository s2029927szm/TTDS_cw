import sys
import t11
import t12
import t13

model=str(sys.argv[1])
content=str(sys.argv[2])
print(model)
print(content)

if model=='111':
    t11.search_lyc(content)
elif model=='222':
    t12.search_art(content)
elif model=='333':
    t13.search_song(content)
else:
    print('wrong model')

