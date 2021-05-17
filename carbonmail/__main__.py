#Arquivo principal a ser executado
#Quando iniciamos o projeto ele é o primeiro ao Python executar
#Nós usamos para ser o ponto de entrada da aplicação

from carbonmail.email_sender.manager import initialize as init_sender

init_sender()