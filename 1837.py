import sys
numeros = input().split()
a,b = list(map(lambda x: int(x),numeros))

maiorValor = max(abs(a),abs(b))
qs = 0
rs = sys.maxsize
r = 0
for q in range(-maiorValor,maiorValor):
    r = (a-b*q)
    if rs >= r and r>0:
        qs = q
        rs = r
print(qs,rs)
