#!/usr/bin/env python3

# Importar biblioteca sys
import sys

# Uso de sys.argv[] para que o usuário dê os lados do triângulo
a = sys.argv[1]
b = sys.argv[2]

# Método isdigit() retorna Verdadeiro para caracteres numéricos e Falso para demais
if a.isdigit() and b.isdigit():
# Verifica se números fornecidos são menores que 500
    if int(a) < 500 and int(b) < 500:
# Calcula área do triângulo pela fórmula do triângulo retângulo
        A = int(a)*int(b)/2
        print('A área do triangulo retângulo com lados a=',a, 'e b=',b,', é', A)
    else:
        print('Números excedem o limite')
else:
    print('Forneça apenas números inteiros')

