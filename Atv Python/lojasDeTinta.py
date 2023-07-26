import math

metros_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade de litros necessários
litros_necessarios = metros_quadrados / 3

# Calculando a quantidade de latas de tinta necessárias (arredondando para cima)
quantidade_latas = math.ceil(litros_necessarios / 18)

# Calculando o preço total
preco_lata = 80.00
preco_total = quantidade_latas * preco_lata

print(f"Quantidade de latas de tinta necessárias: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
