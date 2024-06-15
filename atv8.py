'''
8- Desenvolva um algoritmo que calcule o fatorial de um número fornecido pelo usuário.
Entrada: Um número inteiro.
Saída: O fatorial desse número.

'''
# Solicita ao usuário que informe um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é negativo
if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    # Calcula o fatorial do número usando um loop
    for i in range(1, numero + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"O fatorial de {numero} é {fatorial}")
