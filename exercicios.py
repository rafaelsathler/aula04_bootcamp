# 1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número
# elevado ao quadrado.

#lista = list(range(1,11))
#for i in lista:
#    print(i)

# 2 - Dada a lista ["Python", "Java", "C++", "JavaScript"],
# remova o item "C++" e adicione "Ruby".

#lista: list = ["Python", "Java", "C++", "JavaScript"]
#print(lista)
#n=0
#for i in lista:
#    if i == "C++":
#        lista[n] = "Ruby"
#        n += 1
#    else:
#        n += 1
#print(lista)

# 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

#livro: dict = {
#    "nome": "Game of thrones",
#    "autor": "Estagiario",
#    "ano": 2005
#}

#livro_02: dict = {
#    "nome": "Game of thrones",
#    "autor": "hohohoho",
#    "ano": 2008
#}

#lista: list = []
#lista.append(livro)
#lista.append(livro_02)

#for elemento in lista:
#    print(elemento)

# 4 - Escreva um programa que conta o número de ocorrências 
# de cada caractere em uma string usando um dicionário.

#def contar_caracteres(s):
#    contagem = {}
#    for caractere in s:
#        contagem[caractere] = contagem.get(caractere, 0) + 1
#    return contagem

#print(contar_caracteres("engenharia de dados"))

# 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário
#  {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

#lista_compras = ["maçã", "banana", "cereja"]
#precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#total = sum(precos[item] for item in lista_compras)
#print(f"Preço total: {total}")

# 6 - Objetivo: Dada uma lista de emails, remover todos os duplicados.

#lista_emails: list = ["rafael@com.br", "vera@com.br", "vera@com.br"]
#lista_emails = list(dict.fromkeys(lista_emails))
#print(lista_emails)

#emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#emails_unicos = list(set(emails))

#print(emails_unicos)

# 7 - Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
#import random

#idade = []
#idade = random.sample(range(1, 50), 7)
#lista_idade = []

#print(idade)
#for i in idade:
#    if i >= 18:
#        lista_idade.append(i)
#    else:
#        next
#print(lista_idade)

#ou
#idades = [22, 15, 30, 17, 18]
#idades_validas = [idade for idade in idades if idade >= 18]

#print(idades_validas)

# 8 - Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

#lista: list = [
#    {"nome": "Rafael", "idade": 34},
#    {"nome": "Luan", "idade": 25},
#    {"nome": "Gabriel", "idade": 12}
#]

#lista.sort(key=lambda pessoa: pessoa["nome"])
#print(lista)

# 9 - Objetivo: Dado um conjunto de números, calcular a média.

list_num = [*range(1,11)]
print(list_num)
media = sum(list_num) / len(list_num)
print(f"a soma é {sum(list_num)}, o total de num é {len(list_num)}. Totalizando a média de {media}" )