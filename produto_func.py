import json
from dataclasses import asdict
from Produto import Produto

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o desconto do produto (em %): "))
    return Produto(nome, preco, desconto)

def salvar_produtos(produtos, filename='produtos.json'):
    with open(filename, 'w') as file:
        json.dump([asdict(produto) for produto in produtos], file, indent=4)

def carregar_produtos(filename='produtos.json'):
    try:
        with open(filename, 'r') as file:
            produtos_data = json.load(file)
            return [Produto(**data) for data in produtos_data]
    except FileNotFoundError:
        return []

def listar_produtos(produtos):
    for i, produto in enumerate(produtos):
        print(f"{i}: Produto: {produto.nome}, Preço: {produto.preco:.2f}, Desconto: {produto.desconto*100:.0f}%, Preço com Desconto: {produto.preco * (1 - produto.desconto):.2f}")

def editar_produto(produtos):
    listar_produtos(produtos)
    try:
        indice = int(input("Digite o índice do produto a ser editado: "))
        produto = produtos[indice]
        produto.preco = float(input(f"Digite o novo preço para {produto.nome}: "))
        produto.desconto = float(input(f"Digite o novo desconto para {produto.nome} (em %): ")) / 100
    except (IndexError, ValueError):
        print("Índice inválido. Tente novamente.")
