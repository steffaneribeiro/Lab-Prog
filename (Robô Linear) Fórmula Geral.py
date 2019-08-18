comandos = input()
print ({x:comandos.count(x) for x in set(comandos)})
