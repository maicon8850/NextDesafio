'''
3- Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
Se quantidade <= 5 o desconto será de 2%
Se quantidade > 5 e quantidade <=10 o desconto será de 3%
Se quantidade > 10 o desconto será de 5%

'''
# Solicita a descrição do produto (nome) do usuário
descricao_produto = input("Digite a descrição do produto: ")

# Solicita a quantidade adquirida do produto e converte para inteiro
quantidade = int(input("Digite a quantidade adquirida: "))

# Solicita o preço unitário do produto e converte para float
preco_unitario = float(input("Digite o preço unitário: "))

# Calcula o total (quantidade adquirida * preço unitário)
total = quantidade * preco_unitario

# Determina o desconto com base na quantidade adquirida
if quantidade <= 5:
    desconto = 0.02 * total  # 2% de desconto
elif quantidade <= 10:
    desconto = 0.03 * total  # 3% de desconto
else:
    desconto = 0.05 * total  # 5% de desconto

# Calcula o total a pagar (total - desconto)
total_a_pagar = total - desconto

# Exibe o total, o desconto e o total a pagar
print(f"Descrição do produto: {descricao_produto}")
print(f"Quantidade adquirida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")
