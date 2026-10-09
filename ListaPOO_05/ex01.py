from datetime import datetime, timedelta

s = input("Informe sua data de nascimento dd/mm/aaaa: ")
nasc = datetime.strptime(s, "%d/%m/%Y")
agora = datetime.now()

tempo = agora - nasc
print(tempo)

anos = tempo.days // 365
meses = tempo.days % 365 // 30

print(f"{anos} anos e {meses} mes(es)")



