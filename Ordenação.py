""" 
Insira em uma lista cinco nomes e mostre na ordem alfabética.
"""

import os

os.system("clear")

lista_de_nomes = ["Marta", "Maria", "Renata", "Juliana", "Marcela"]

nova_lista = sorted(lista_de_nomes)

for nome in nova_lista:
    print(nome)