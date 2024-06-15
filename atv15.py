'''
15- A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto.
 Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. 
 O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não” . Informar total de carros com ano até 2000 e total geral.

'''
total_ate_2000 = 0
total_geral = 0
continuar = 'S'

while continuar == 'S':
    ano = int(input("Digite o ano do veículo: "))
    
    if ano <= 2000:
        desconto = 0.12
        total_ate_2000 += 1
    else:
        desconto = 0.07
    
    valor_veiculo = float(input("Digite o valor do veículo: "))
    valor_desconto = valor_veiculo * desconto
    valor_pago = valor_veiculo - valor_desconto
    
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")
    
    total_geral += 1
    continuar = input("Deseja continuar calculando descontos? (S/N) ").upper()

print(f"Total de carros até 2000: {total_ate_2000}")
print(f"Total geral de carros: {total_geral}")
