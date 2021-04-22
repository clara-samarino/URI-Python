
ponto1 = input()
p1X, p1Y = ponto1.split()
ponto2 = input()
p2X, p2Y = ponto2.split()
distancia = pow(pow((float(p2X) - float(p1X)),2) + pow((float(p2Y) - float(p1Y)),2),1/2)
print("%.4f" %distancia)