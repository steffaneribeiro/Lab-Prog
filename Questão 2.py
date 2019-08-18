comandos = input()
F = 0
T = 0
for i in comandos:
    if i =='F':
        F+=1
    else:
        T+=1
if T ==F:
    print("A posição final do robô é IGUAL a posição inicial.")
else:
    print("A posição final do robô é DIFERENTE da posição inicial.")
