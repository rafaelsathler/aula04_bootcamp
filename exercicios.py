# 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {
    "nome": "Game of thrones",
    "autor": "Estagiario",
    "ano": 2005
}

livro_02: dict = {
    "nome": "Game of thrones",
    "autor": "hohohoho",
    "ano": 2008
}

lista: list = []
lista.append(livro)
lista.append(livro_02)

for elemento in lista:
    print(elemento)