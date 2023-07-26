print("Cálculo do Peso Ideal")
altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (M para masculino ou F para feminino): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    genero = "feminino"
else:
    print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
    exit()

print(f"Para uma pessoa do sexo {genero}, o peso ideal é: {peso_ideal:.2f} kg")
