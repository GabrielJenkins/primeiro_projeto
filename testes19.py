carros = ("corsa","uno","bmw","ferrari","bentley")
carros_lista = list(carros)
print(type(carros_lista))#'list'
carros_lista.extend(['calhambeque','camaro'])
carros_lista.pop(0)
carros_lista.pop()
print(carros_lista[0])
print(len(carros_lista))
dicionario = {
    "nome": "Gabriel" ,
    "idade" : 22 ,
    "profissão" : "QA"
}
print(dicionario["nome"])