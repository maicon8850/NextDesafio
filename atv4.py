'''
4- Crie um algoritmo que peça ao usuário que informe 10 números inteiros e armazene-os em um vetor. 
A seguir, apresente a multiplicação de todos os elementos pares e a soma de todos os elementos ímpares.

'''
# Inicializa um vetor para armazenar os 10 números inteiros
numeros = []

# Inicializa variáveis para a multiplicação dos pares e soma dos ímpares
multiplicacao_pares = 1
soma_impares = 0

# Solicita ao usuário que informe 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)  # Adiciona o número ao vetor

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        multiplicacao_pares *= numero  # Multiplica se o número for par
    else:
        soma_impares += numero  # Soma se o número for ímpar

# Exibe a multiplicação dos números pares e a soma dos números ímpares
print(f"Multiplicação de todos os elementos pares: {multiplicacao_pares}")
print(f"Soma de todos os elementos ímpares: {soma_impares}")

