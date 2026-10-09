#!/usr/bin/env python3

#CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATGTGTGAGCCGACGAAAAGTAAAAGAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA

import sys

#usar len(dna) para ver se os números são maiores que a sequência
#pra extrair a sequência com numeros da linha de comando, eu acredito que seja necessário criar alguma lista ou conjunto ou dicionário
#para colocar o resultado da interação

#na verdade acho que não. acho que eu preciso imprimir com a sequência [sys.argv[]:sys.argv[]] mas o foda é que não sei oq colocar antes

#3. O script tem que extrair a sequência da CDS 1, e conferir se inicia com o códon de inicio, ATG.

#s.startswith('other_string')

#7 argumentos argv.sys
dna = sys.argv[1]
primeiro = int(sys.argv[2]) -1
segundo = int(sys.argv[3]) 
terceiro = int(sys.argv[4]) -1
quarto = int(sys.argv[5]) 
quinto = int(sys.argv[6]) -1
sexto = int(sys.argv[7]) 


if dna.isalpha():
    CDS_1 = dna[primeiro:segundo]
    if CDS_1.startswith('ATG'):
        CDS_2 = dna[terceiro:quarto]
        CDS_3 = dna[quinto:sexto]
        if CDS_3.endswith('TAG') or CDS_3.endswith('TAA') or CDS_3.endswith('TGA'):
            print('Gene: ',CDS_1 + CDS_2 + CDS_3)
        else:
            print('Sequência final não contém códon de término')
    else:
        print('Sequência inicial não contém códon de início "ATG"')
else:
    print('Sequência fornecida não é formada por letras')




# print(dna[primeiro:segundo])


# if dna.isalpha():
# seq = []

# for nt in dna:
#     nt += 1

