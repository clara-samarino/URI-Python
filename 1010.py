linha1 = input()
vetor = linha1.split()
quantidade1 = float(vetor[1])
valorunitario1 = float(vetor[2])
#print(quantidade1*valorunitario1)

linha2 = input()
vet = linha2.split()
quantidade2 = float(vet[1])
valorunitario2 = float(vet[2])
total = (quantidade1*valorunitario1 + quantidade2*valorunitario2)

print("VALOR A PAGAR: R$ %.2f" %total)

