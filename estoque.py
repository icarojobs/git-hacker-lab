PRODUTOS = []


def adicionar(nome, qtd):
    PRODUTOS.append({"nome": nome, "qtd": qtd})
    return PRODUTOS


def baixa(nome, quantidade):
    if quantidade <= 0:
        raise ValueError(f"quantidade invalida: {quantidade}")
    for p in PRODUTOS:
        if p["nome"] == nome:
            p["qtd"] -= quantidade
    return PRODUTOS


def aplicar_desconto(preco, percentual):
    return preco - (preco * percentual / 100)
