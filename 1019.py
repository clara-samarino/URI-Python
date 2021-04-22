segundos = float(input())
horas = 0
minutos = 0
seg = 0

if segundos>=3600:
    horas = int(segundos/3600)
    if segundos%3600>60:
        minutos = int((segundos-horas*3600)/60)
        seg = int(segundos - horas*3600 - minutos*60)
    else:
        seg = int(segundos%3600)
elif segundos>=60:
    minutos = int(segundos/60)
    seg = int(segundos%60)
else:
    seg = segundos

print("%d:%d:%d" %(horas,minutos,seg))
