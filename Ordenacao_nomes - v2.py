"""
Solicite que o usuário insira em uma lista cinco nomes
e mostre na ordem alfabética.
"""
import os

os.system("clear")

# Criando lista.
lista_de_nomes = []

#Solicitando cinco nomes ao usuário.
for i in range (5):
    nome = input("Digite um nome: ")
    lista_de_nomes.append(nome)

#Ordenando lista
lista_ordenada = sorted(lista_de_nomes)

print("\nExibindo nomes em ordem alfabética: ")
for nome in lista_ordenada:
    print(nome)