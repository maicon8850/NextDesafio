'''
7-  Desenvolva um algoritmo que conte quantas vogais existem em uma string fornecida pelo usuário.
Entrada: Uma string.
Saída: O número de vogais na string.

'''
# Solicita ao usuário que informe uma string
string = input("Digite uma string: ")

# Inicializa um contador de vogais
contador_vogais = 0

# Define um conjunto de vogais
vogais = "aeiouAEIOU"

# Itera através dos caracteres da string
for char in string:
    if char in vogais:
        contador_vogais += 1  # Incrementa o contador se o caractere for uma vogal

# Exibe o número de vogais na string
print("Número de vogais na string:", contador_vogais)
