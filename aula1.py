# Variáveis 

# Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 # float
# Valores boleanos
esta_aberto = True
# Strings
nome_do_curso = "Lógica de Programação"

# Como varáiveis seriam usadas em um programa real?
# Problema 1 - Valor por hora 
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas você trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)