print("NOTA FINAL DO TRABALHO DE HISTÓRIA!")

nota1 = float(input("Nota: Conteúdo: "))
nota2 = float(input("Nota: Qualidade do material: "))
nota3 = float(input("Nota: Entendimento do conteúdo: "))
nota4 = float(input("Nota: Apresentação: "))

print(f"Olá, Caíque. Sua média é: {float(nota1 + nota2 + nota3 + nota4) / 4}.")

teste = type(nota1)
print(teste)