def time_aleatorio(matricula):
    if matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

perguntar_numero = int(input("Qual é o seu número de matrícula?: "))
time_aleatorio(perguntar_numero)