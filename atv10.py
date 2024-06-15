'''
10- Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. 
Apresentar os valores trocados.
'''
# Ler os valores das variáveis A e B do usuário
A = input("Digite o valor de A: ")
B = input("Digite o valor de B: ")

# Mostrar os valores originais de A e B
print(f"Valores originais: A = {A}, B = {B}")

# Trocar os valores de A e B
A, B = B, A

# Mostrar os valores trocados de A e B
print(f"Valores trocados: A = {A}, B = {B}")
