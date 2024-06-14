"""
1- Aplicar um algoritmo que calcule a média das notas bimestrais de uma escola (media = (nota1 + nota2 + nota3 + nota4)/4). 
O algoritmo deve repetir o cálculo até que o usuário responda “N” à pergunta “Deseja continuar (S/N) ?”. 

"""
while True:
    n1 = float(input('Primeira nota do aluno: '))  # float(numero ponto flutuante)
    n2 = float(input('Segunda nota do aluno: '))   # input(faz com que meu teclado entre)
    n3 = float(input('Terceira nota do aluno: '))
    n4 = float(input('Quarta nota do aluno: '))
    
    media = (n1 + n2 + n3 + n4) / 4
    print('A média entre {}, {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, n4, media))
    
    continuar = input('Deseja continuar (S/N)? ').strip().upper()
    if continuar == 'N':
        break
