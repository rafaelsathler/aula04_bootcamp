import json

produto_01: dict = {
    "nome": "Sapato",
    "quantidade": 10,
    "preco": 55.40,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Televisão",
    "quantidade":5,
    "preco": 103.55,
    "disponibilidade": False    
}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)  #linguagem javascript
print(carrinho_json)