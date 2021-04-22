idadedias = int(input())
idadeano = 0
idademeses = 0
idadedia = 0
if idadedias >= 365:
    idadeano = int(idadedias/365)
if idadedias - 365*idadeano >= 30:
    idademeses = int((idadedias%365)/30)
idadedia = idadedias - idadeano*365 - idademeses*30
print("%d ano(s)" %idadeano)
print("%d mes(es)"%idademeses)
print("%d dia(s)" %idadedia)