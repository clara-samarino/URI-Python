
linha = input().split()
# print(type(linha))
A,B,C = list(map(lambda x: float(x),linha))

pi = 3.14159
aTrianguloAC = A*C/2.0
aCirculoC = pi*pow(C,2)


aTrapezio = ((A+B)*C)/2.0
aQuadrado = B*B
aRetangulo = A*B
print("TRIANGULO: %.3f \nCIRCULO: %.3f \nTRAPEZIO: %.3f \nQUADRADO: %.3f \nRETANGULO: %.3f" 
%(aTrianguloAC, aCirculoC, aTrapezio, aQuadrado, aRetangulo))
