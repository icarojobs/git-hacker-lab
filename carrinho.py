"""Carrinho de compras — usado pela loja."""

FRETE_FIXO = 20.00
FRETE_GRATIS_ACIMA_DE = 200.00


def subtotal(itens):
    return sum(i["preco"] * i["qtd"] for i in itens)


def frete(itens):
    # BUG: usa > em vez de >=, então um pedido de exatamente R$ 200 paga frete
    return 0.0 if subtotal(itens) > FRETE_GRATIS_ACIMA_DE else FRETE_FIXO


def total(itens):
    return subtotal(itens) + frete(itens)
