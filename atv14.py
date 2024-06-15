'''
14-  Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa.
Considere a idade a partir de 18 anos como maior de idade.

'''
# Definir o número de pessoas
num_pessoas = 75

# Loop para iterar sobre cada pessoa
for pessoa in range(1, num_pessoas + 1):
    # Entrada da idade da pessoa
    idade = int(input(f"Digite a idade da pessoa {pessoa}: "))
    
    # Verificar se é maior ou menor de idade
    if idade >= 18:
        print(f"Pessoa {pessoa}: Maior de idade")
    else:
        print(f"Pessoa {pessoa}: Menor de idade")
