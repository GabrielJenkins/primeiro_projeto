nome = input("Qual é o seu nome?: ")
mes = input("Em que mês realizaste a compra?: ")
valor_compra = float(input("Qual é o valor de sua compra?: "))
desconto = 10
cupom_de_desconto = "É10"

print(f"Olá {nome}. Em {mes} você realizou uma compra no valor de R${valor_compra} e ganhou um cupom de desconto no valor de {desconto}% em sua próxima compra. Use o cupom {nome}{cupom_de_desconto}")

cupom_input = input("Insira seu cupom de desconto: ")

porcentagem_desconto = (valor_compra*desconto)/100

print(f"Sua compra após o cupom de desconto é de: R${valor_compra - porcentagem_desconto}.")

print(f"O valor original da compra é R${valor_compra}. Com um desconto de {desconto}%, o preço final é R${valor_compra * (1 - desconto / 100):.2f}.")


tipo_nome = type(nome)
tipo_mes = type(mes)
tipo_valor_compra = type(valor_compra)
tipo_desconto = type(desconto)
tipo_cupom = type(cupom_de_desconto)

print(tipo_nome,"|",tipo_mes,"|",tipo_valor_compra,"|",tipo_desconto,"|",tipo_cupom)