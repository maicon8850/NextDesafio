'''
12- O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o resultado). 
Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que leia o custo de fábrica de um carro e informe o custo ao consumidor do mesmo. 

'''
# Entrada do custo de fábrica do carro
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# Calcular os impostos (45% do custo de fábrica)
impostos = 0.45 * custo_fabrica

# Calcular a percentagem do distribuidor (28% sobre o custo de fábrica + impostos)
percentual_distribuidor = 0.28 * (custo_fabrica + impostos)

# Calcular o custo ao consumidor (custo de fábrica + impostos + percentual do distribuidor)
custo_consumidor = custo_fabrica + impostos + percentual_distribuidor

# Exibir o custo ao consumidor formatado
print(f"O custo ao consumidor do carro será: R$ {custo_consumidor:.2f}")
