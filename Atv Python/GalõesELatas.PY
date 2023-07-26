import math

metros_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de litros necessários com 10% de folga
litros_necessarios = metros_quadrados / 6 * 1.1

# Quantidade de latas e galões necessários
quantidade_latas = math.ceil(litros_necessarios / 18)
quantidade_galoes = math.ceil(litros_necessarios / 3.6)

# Preços
preco_lata = 80.00
preco_galao = 25.00

# Preço total comprando apenas latas
preco_total_latas = quantidade_latas * preco_lata

# Preço total comprando apenas galões
preco_total_galoes = quantidade_galoes * preco_galao

# Misturando latas e galões
quantidade_latas_mistura = math.floor(litros_necessarios / 18)  # Quantidade inteira de latas
resto_litros = litros_necessarios - (quantidade_latas_mistura * 18)  # Litros restantes após usar latas inteiras

# Quantidade de galões necessários para o resto dos litros
quantidade_galoes_mistura = math.ceil(resto_litros / 3.6)

# Preço total misturando latas e galões
preco_total_mistura = (quantidade_latas_mistura * preco_lata) + (quantidade_galoes_mistura * preco_galao)

print(f"Quantidade de latas de tinta necessárias: {quantidade_latas}")
print(f"Preço total comprando apenas latas: R$ {preco_total_latas:.2f}")

print(f"Quantidade de galões de tinta necessários: {quantidade_galoes}")
print(f"Preço total comprando apenas galões: R$ {preco_total_galoes:.2f}")

print(f"Quantidade de latas de tinta na mistura: {quantidade_latas_mistura}")
print(f"Quantidade de galões de tinta na mistura: {quantidade_galoes_mistura}")
print(f"Preço total misturando latas e galões: R$ {preco_total_mistura:.2f}")
