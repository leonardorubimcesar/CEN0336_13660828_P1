#!/usr/bin/env python3
 
# Cria um dicionário vazio
contagem = {} 

# Função input permite que o usuário forneça a sequência 
seq = input('Insira seu valor:')
print("Contagem de nucleotídeos: ",)

# Função set() retorna um conjunto, que contém apenas caracteres únicos da sequência fornecida
unique = set(seq)

# if/else é usado aqui para avisar o usuário caso ele forneça uma sequência diferente de uma sequência de letras, com o método isalpha()
if seq.isalpha():
    for nt in seq:
# Primeiro vamos armazenar a contagem de nucleotídeos em count
        count = seq.count(nt)
# E então adicionar esses valores ao dicionário contagem
        contagem[nt] = count
else:
    print('Digite letras apenas')
# Agora será iterado cada dupla do dicionário
for nt in contagem:
    print(nt, ":", " ", contagem[nt], sep="")