#!/bin/bash

echo '---pasta atual---' #echo permite imprimir stings no terminal
pwd #mostra pasta atual
echo '---conteúdo da pasta HOME---'
cd ~ #muda pasta para home
ls -F #mostra conteúdo detalhado da pasta no terminal
ls -F > lista_HOME.txt #redireciona o conteúdo da pasta no arquivo
cat < lista_HOME.txt  #salva conteúdo redirecionado
mv /home/leonardo_rubim/lista_HOME.txt /home/leonardo_rubim/CEN0336_13660828_P1 #muda o arquivo para esse repositório
echo '---data atual---'
date #mostra a data atual em inglês: dia da semana + mês + hora + fuso-horário + ano