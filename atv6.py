'''
6- Escreva um programa que leia uma lista de números e os ordene em ordem crescente.
Entrada: Uma lista de números.
Saída: A lista de números ordenada.

'''
# Solicita ao usuário que informe uma lista de números separados por espaço
numeros = input("Digite uma lista de números separados por espaço: ")

# Converte a string de entrada em uma lista de inteiros
lista_numeros = list(map(int, numeros.split()))

# Ordena a lista de números em ordem crescente
lista_numeros.sort()

# Exibe a lista de números ordenada
print("Lista de números ordenada:", lista_numeros)
