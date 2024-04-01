b1 = float(input('digite a nota da prova b1:'))
b2 = float(input('digite a nota da prova b2:'))
media = (b1+b2) / 2
if media > 7:
    print("esta aprovado")
else:
    print('esta reprovado')

print(f'sua media eh : {media:.2f}')

