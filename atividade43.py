###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

qh = float(input("digite a quantidade de hamburguer: "))
qf = float(input("digite a quantidade de fritas: "))
qc = float(input("digite a quantidade de chesseburguer: "))
qr = float(input("digite a quantidade de refrigerante: "))
qm = float(input("digite a quantidade de milkshake: "))
t = (qh * 3.00) + (qf * 2.50) +(qc * 2.50) + (qr * 1.00) + (qm * 3.00)
print(f"o valor da conta {t:.2f}")