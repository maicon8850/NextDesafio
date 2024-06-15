'''
9- Escreva um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os seguintes critérios:
50% para aqueles que ganham menos do que 3 salários mínimos
20% para aqueles que ganham entre 3 a 10 salários mínimos
15% para aqueles que ganham de 10 a 20 salários mínimos
10% para os demais

'''
salarios = [1500, 5000, 15000, 25000]  # Exemplo de salários dos funcionários
salario_minimo = 1100  # Exemplo de salário mínimo

salarios_reajustados = []

for salario in salarios:
    if salario < 3 * salario_minimo:
        novo_salario = salario * 1.5  # Reajuste de 50% para salários abaixo de 3 salários mínimos
    elif 3 * salario_minimo <= salario <= 10 * salario_minimo:
        novo_salario = salario * 1.2  # Reajuste de 20% para salários entre 3 e 10 salários mínimos
    elif 10 * salario_minimo < salario <= 20 * salario_minimo:
        novo_salario = salario * 1.15  # Reajuste de 15% para salários entre 10 e 20 salários mínimos
    else:
        novo_salario = salario * 1.1  # Reajuste de 10% para salários acima de 20 salários mínimos
    
    salarios_reajustados.append(round(novo_salario, 2))

print("Salários reajustados:", salarios_reajustados)
 