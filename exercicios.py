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

#list_num = [*range(1,11)]
#print(list_num)
#media = sum(list_num) / len(list_num)
#print(f"a soma é {sum(list_num)}, o total de num é {len(list_num)}. Totalizando a média de {media}" )

# 10 - Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares

#lista_dados: int = [*range(1,11)]

#pares = [valor for valor in lista_dados if valor % 2 == 0]
#impar = [valor for valor in lista_dados if valor % 2 != 0]
#resultado: list = []
#resultado.append(pares)
#resultado.append(impar)

#print(resultado)

# 11 - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

#produtos = [
#    {"id": 1, "nome": "teclado", "valor": 100}, 
#    {"id": 2, "nome": "mouse", "valor": 50}, 
#    {"id": 3, "nome": "headphone", "valor": 200}, 
#]

#for produto in produtos:

#    if produto["id"] == 2:
#        produto["valor"] = 300

#print(produtos)

#12 - Dados dois dicionários, fundi-los em um único dicionário.

#dic_01 = {"a": 1,"b": 1500}
#dic_02 = {'c': 2,"d": 800}
#consolidado = {**dic_01, **dic_02}
#print(consolidado)

#dic_02.update(dic_01)
#print(dic_02)

#13- Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

#estoque: dict = {"mouse": 30, "teclado": 100, "monitor": 0}

#estoque_acima = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
#print(estoque_acima)

#14 - Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())
print(chaves)
print(valores)