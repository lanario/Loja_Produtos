from dataclasses import dataclass, asdict
import json
from produto_func import carregar_produtos, adicionar_produto, salvar_produtos, listar_produtos, editar_produto
from Produto import Produto


# Lista para armazenar os produtos
lista_produtos = carregar_produtos()

# Loop para adicionar, listar, editar produtos
while True:
    opcao = input("Escolha uma opção: adicionar (a), listar (l), editar (e), sair (s): ").lower()
    if opcao == 'a':
        produto = adicionar_produto()
        lista_produtos.append(produto)
        salvar_produtos(lista_produtos)
    elif opcao == 'l':
        listar_produtos(lista_produtos)
    elif opcao == 'e':
        editar_produto(lista_produtos)
        salvar_produtos(lista_produtos)
    elif opcao == 's':
        break
    else:
        print("Opção inválida. Tente novamente.")