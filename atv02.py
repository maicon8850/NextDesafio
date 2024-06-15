'''
2- Calcule quantos azulejos são necessários para azulejar uma parede. 
É necessário conhecer a altura da parede (AP), a sua largura (LP), e a altura do azulejo (A) e sua largura (LA). Leia os dados através do teclado. 

'''
# Solicita os dados de entrada do usuário
altura_parede = float(input("Digite a altura da parede (em metros): "))
largura_parede = float(input("Digite a largura da parede (em metros): "))
altura_azulejo = float(input("Digite a altura do azulejo (em metros): "))
largura_azulejo = float(input("Digite a largura do azulejo (em metros): "))

# Calcula a área da parede
area_parede = altura_parede * largura_parede

# Calcula a área de um azulejo
area_azulejo = altura_azulejo * largura_azulejo

# Calcula a quantidade de azulejos necessária
quantidade_azulejos = area_parede / area_azulejo

# Arredonda para cima para garantir que toda a parede seja coberta
import math
quantidade_azulejos = math.ceil(quantidade_azulejos)

# Exibe o resultado
print(f"Serão necessários {quantidade_azulejos} azulejos para cobrir a parede.")4,