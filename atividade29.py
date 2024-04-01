###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

dias = float(input("quantos dias o encanador trabalhou: "))
salariob = dias*30
descontop = salariob * 0.11
salariop = descontop - salariob 

descontoi = salariop * 0.07
salarioi = descontoi - salariop 
print(f"o salario final do encanador eh : {salarioi:.2f}")
