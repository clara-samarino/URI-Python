valor = int(input())
valorResidual = valor
quantNotas = 0
notas = [100,50,20,10,5,2,1]
print(valor)
for nota in notas:
    quantNotas = (valorResidual - valorResidual%nota)/nota
    valorResidual = valorResidual - quantNotas*nota
    print("%d nota(s) de R$ %d,00" %(quantNotas, nota))

