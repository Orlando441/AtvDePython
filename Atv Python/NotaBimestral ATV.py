
print("Digite as 4 notas bimestrais:")
notas1 = float(input("Digite a primeira nota válida (número): "))
notas2 = float(input("Digite a segunda nota válida (número): "))
notas3 = float(input("Digite a terceira nota válida (número): "))
notas4 = float(input("Digite a quarta nota válida (número): "))

soma = notas1 + notas2 + notas3 + notas4
media = soma / 4
mensagem = f"A média das notas é {media:.2f}"  # Rounded to two decimal places
print(mensagem)

