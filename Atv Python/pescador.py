limite_peso = 50  # Limite de peso estabelecido pelo regulamento (em quilos)
valor_multa_por_quilo = 4.00  # Valor da multa por quilo excedente (em reais)

peso = float(input("Digite o peso de peixes pescados (em quilos): "))

if peso <= limite_peso:
    excesso = 0  # Não há excesso de peso
    multa = 0  # Não há multa
else:
    excesso = peso - limite_peso
    multa = excesso * valor_multa_por_quilo

print(f"Peso de peixes pescados: {peso:.2f} kg")
if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("Não há excesso de peso. Nenhuma multa a pagar.")
