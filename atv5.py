'''
5- Desenvolva um algoritmo que leia uma string e determine se ela é um palíndromo.
Entrada: Uma string.
Saída: "É um palíndromo" ou "Não é um palíndromo".

'''
# Solicita ao usuário que informe uma string
string = input("Digite uma string: ")

# Remove espaços e converte para minúsculas para a comparação
string_limpa = ''.join(string.lower().split())

# Verifica se a string limpa é igual à sua versão invertida
if string_limpa == string_limpa[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
