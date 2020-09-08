line = lambda x: print("#"*x)
line(12)

sumar = lambda x: x+1

lista = [1.2,3.2,4,3.1,2.2]

mapear = list(map(sumar, lista))

print(mapear)

listaNum = [12,3214,45,4213,12,32,2,1,112,4,4,545,34,4]

par = lambda x: x%2 == 0
pares = list(filter(par, listaNum))
print(pares)