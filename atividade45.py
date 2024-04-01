###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

nome_aluno = input("digite o nome do aluno:")
nota_qualitativa = float(input("digite a nome da prova qualitativa: "))
nota_prova = float(input("digite a nota da prova: "))
media = (nota_qualitativa + (nota_prova * 2)) / 3
print(f"a media do aluno {nome_aluno} eh: {media:.2f}")