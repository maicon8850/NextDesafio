'''
13-  Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre.
Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media maior ou igual 7), Reprovado (media <= 5) e Recuperação (média entre 5.1 a 6.9).

'''
# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular média
media = (nota1 + nota2 + nota3) / 3

# Determinar menção
if media >= 7:
    mencao = "Aprovado"
elif media <= 5:
    mencao = "Reprovado"
else:
    mencao = "Em recuperação"

# Exibir resultados
print(f"Nome do aluno: {nome_aluno}")
print(f"Menção: {mencao}")
