#!/usr/bin/env python3

# 1º: importar a biblioteca sys
import sys

#2º sequência de nucleotídeos mais a posição de início e término na sequência dada pelo usuário na linha de comando
dna = sys.argv[1]
#para os nucleotídeos de início, subtrai-se 1 do valor do usuário, visto que as listas são contadas a partir do valor 0. Assim, o '20' dado pelo usuário na verdade
#representa a posição 19 
primeiro = int(sys.argv[2]) -1
segundo = int(sys.argv[3]) 
terceiro = int(sys.argv[4]) -1
quarto = int(sys.argv[5]) 
quinto = int(sys.argv[6]) -1
sexto = int(sys.argv[7]) 

#3º confere se o input do usuário para o gene é uma string
if type(dna) == str:
    CDS_1 = dna[primeiro:segundo]
#4º confere se gene começa com códon de início
    if CDS_1.startswith('ATG'):
        CDS_2 = dna[terceiro:quarto]
        CDS_3 = dna[quinto:sexto]
#5º confere se gene termina com códon de término
        if CDS_3.endswith('TAG') or CDS_3.endswith('TAA') or CDS_3.endswith('TGA'):
#º6 concatena gene
            print('Gene: ',CDS_1 + CDS_2 + CDS_3)
        else:
            print('Sequência final não contém códon de término')
    else:
        print('Sequência inicial não contém códon de início "ATG"')
else:
    print('Sequência fornecida não é formada por letras')
