comandos = input()
dist = 0
for i in comandos:
    if i == 'F':
        dist+=1
    else:
        dist-=1
print(dist)
