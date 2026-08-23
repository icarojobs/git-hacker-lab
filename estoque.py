PRODUTOS = []


def adicionar(nome, qtd):
    PRODUTOS.append({"nome": nome, "qtd": qtd})
    return PRODUTOS


def baixa(nome, quantidade):
    for p in PRODUTOS:
        if p["nome"] == nome:
            p["qtd"] -= quantidade
    return PRODUTOS


def relatorio():
    # TODO: agrupar por categoria
    return len(PRODUTOS)
