with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
from itertools import product

def string_para_lista(string):
    # Divide a string em linhas
    linhas = string.splitlines()
    # Inicializa uma lista vazia para armazenar as sublistas
    lista = []

    for linha in linhas:
        # Divide cada linha em elementos separados por vírgula
        elementos = linha.split(",")

        # Adiciona a sublista à lista principal
        lista.append(elementos)

    return lista

def converter_itens_para_set(lista):
    for i in range(len(lista)):
      lista[i] = set(lista[i])
    return lista
def produto_cartesiano(set1, set2):
    return {(a, b) for a in set1 for b in set2}

    

conteudo_convertido = string_para_lista(conteudo)
lista_set = converter_itens_para_set(conteudo_convertido)

for i in range(len(lista_set)):
  if(lista_set[i]==set("U")):
    print(lista_set[i+1].union(lista_set[i+2]))
  elif(lista_set[i]==set("I")):
    print(lista_set[i+1].intersection(lista_set[i+2]))
  elif(lista_set[i]==set("D")):
    print(lista_set[i+1].difference(lista_set[i+2]))
  elif(lista_set[i]==set("C")):
    print(produto_cartesiano(lista_set[i+1],(lista_set[i+2])))
