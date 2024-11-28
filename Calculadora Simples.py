#CALCULADORA SIMPLES

import sys

#Funções que a calculadora vai ultilizar para fazer os calculos

def soma(n1, n2):
     resultado = n1 + n2
     return print("O reultado é: ", resultado)
    
def subtração(n1, n2):
     resultado = (n1) - (n2)
     return print('O resultado é: ', resultado)
    
def multiplicação(n1, n2):
     resultado = (n1) * (n2)
     return print('O resultado é: ', resultado)
    
def divisão(n1, n2):
     resultado = (n1) / (n2)
     return print('O resultado é: ', resultado)

#Coleta dos dados que farão parte do calculo

n1 = int(input('Digite o primeiro valor: '))
if n1 == 0:
     print('Valor invalido(Deve ser maior que zero))')
     sys.exit()

sinal = input('Qual tipo de conta deseja realizar?: + - * /')
if sinal not in ['+', '-', '*', '/']:
     print('Sinal invalido')
     sys.exit()
       
n2 = int(input('Digite o primeiro valor: '))
if n2 == 0:
     print('Valor invalido(Deve ser maior que zero))')
     sys.exit()


if sinal == '+':
     soma(n1, n2)
elif sinal == '-':
     subtração(n1, n2)
elif sinal == '*':
     multiplicação(n1, n2)
elif sinal == '/':
     divisão(n1, n2)
else:
     print('Operação invalida')
     sys.exit()
