###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

g1 = float(input("digite a nota da prova g1:"))
g2 = float(input("digite da nota da prova g2:"))
media = (g1+(g2*2)) / 3
print(f"sua media eh: {media:.2f}")
if media > 7:
    print("voce esta aprovado")
else:
    print("voce esta reprovado")