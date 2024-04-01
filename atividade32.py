###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

valorp = float(input("digite o valor do produto: "))
desconto = valorp * 0.10
valordesc =  desconto - valorp
valorparcela = valorp / 3
comissaocomd = valordesc * 0.05
comissaosemd = valorp * 0.05
print(f"o valor do produto com desconto {valordesc:.2f}")
print(f"valor de cada parcela eh: {valorparcela:.2f}")
print(f"a comissao do vendedor na compra a vista eh : {comissaocomd:.2f}")
print(f"o valor da comissao do vendedor na compra parcelada eh : {comissaosemd:.2f}")