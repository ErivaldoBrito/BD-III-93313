import os
import time
os.system("cls")
""" 
Criando uma função para contagem regressiva.
Iniciando contagem com o número 10.
"""
# Criando lista.
contagem_regressiva = []

#Inciando contagem com o numero 10.
#def contagem_regressiva(numero):
#    for i in range (numero, 0, -1):
#       print(i)
#       time.sleep(1)

def contagem_regressiva(numero):
    if numero < 0:
        return # sair da função
    print(numero)
    time.sleep(1)
    contagem_regressiva(numero - 1)


contagem_regressiva(10)    

