import json

def read_PORT(na_nf):
  return na_nf

def write_PORT(porta, valor):
  if porta:
    return valor
  else:
    return not_func(valor)

def not_func(number):
  if number >= 1:
    return 0
  else:
    return 1

valor = 0
saida = dict()
saidas = list()

lista_obj = list()
lista_obj_paralelos = list()

# Transformando arquivo json em objeto json pra poder usar.
with open('portas.json') as arquivo:
  portas = json.load(arquivo)

with open('grafo.json') as arquivo:
  grafo = json.load(arquivo)

#IDENTIFICAR SAIDA
for obj in portas:
  if obj['I/O'] == 0:
    saida['PORTA'] = obj['PORT']
    saida['NA/NF'] = obj['NA/NF']
    saida['OBJ'] = obj['OBJ']
    break

#Percorrer o dicionário grafo
#Percorrer cada item da lista de cada obj
#Percorrer o vetor do grafo e identificar os objetos que eu fico em paralelo (fazer uma lista com só o valor)
#Dar append de cara porta em portas
for obj in grafo:
  for index, paralelo in enumerate(obj):
    if paralelo:
      index_item_novo = index
      lista_obj_paralelos.append(index_item_novo)
  lista_obj.append(lista_obj_paralelos.copy())
  lista_obj_paralelos.clear()

print(saida)
print(lista_obj)

#ATE AQUI TA TUDO OKAY

#Percorrer o lista obj
#Somar se em paralelo, multiplicar se em série
#Escrever na porta no fim do loop
while(True):
  for index, item in enumerate(lista_obj):
    if item:                                            #se aquele item nao ta vazio, entra no for
      for paralel in item:
        result = result + read_PORT(portas[paralel])            #soma os valores da branch em questão, um OR
      valor = valor * result                            #soma na variavel valor, já que essa branch ta em OR com o resto
    else:
      valor = valor * read_PORT(portas[index])  #se nao tem nda em paralelo, é um AND apenas do valor
  write_PORT(saida, valor)
