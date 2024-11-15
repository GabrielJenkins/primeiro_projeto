nome_cachorro = input("Qual é o nome do seu Doguinho?: ")
idade_cachorro = int(input("Qual é a idade do seu Doguinho?: "))
calculo_idade = idade_cachorro*7
porte_pet = int(input("Qual é o porte do seu cachorro? Selecione um número: \n 1:Pequeno \n 2:Médio \n 3:Grande \n: "))
quantia_banhos = int(input("Quantas vezes, em média, seu Doguinho toma banho a cada 12 meses?: "))

if porte_pet == 1 :
    porte_pq = float(50-5)*quantia_banhos
    print(f"Olá! O(a) {nome_cachorro} tem {calculo_idade} anos e, nos últimos 12 meses, o lucro com este animal foi de R${porte_pq}.")
elif porte_pet == 2 :
    porte_md = float(60-15)*quantia_banhos
    print(f"Olá, {nome_cachorro} tem {calculo_idade} anos e, nos últimos 12 meses, o lucro com este animal foi de R${porte_md}.")
elif porte_pet == 3 :
    porte_gr = float(75-20)*quantia_banhos
    print(f"Olá, {nome_cachorro} tem {calculo_idade} anos e, nos últimos 12 meses, o lucro com este animal foi de R${porte_gr}.")
else :
    print(">>Opção Inválida! Altere o número referente ao porte do seu Doguinho.<<")


