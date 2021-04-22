linha = input().split()
A,B,C = list(map(lambda x: int(x),linha))
maior = (A + B + abs(A-B))/2
maior = (maior + C + abs(maior-C))/2
print("%d eh o maior" %int(maior))