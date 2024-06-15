'''
11- Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. 
Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

'''
# Solicitar o preço de custo e o percentual de acréscimo ao usuário
preco_custo = float(input("Digite o preço de custo do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo (%): "))

# Calcular o valor de venda
valor_venda = preco_custo * (1 + percentual_acrescimo / 100)

# Exibir o valor de venda
print(f"O valor de venda do produto será: R$ {valor_venda:.2f}")
