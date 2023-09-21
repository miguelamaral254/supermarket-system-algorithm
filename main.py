from dataclasses import dataclass

carrinhoDeCompras = {}

@dataclass
class Item:
    nome: str = "#####"
    preco: float = 0


while True:
    print("----------------------------------------------")
    print("1 - adicionar um item")
    print("2 -  remover um item")
    print("3 - alterar um item")
    print("4 - visualizar seu carrinho de compras")
    print("5 - sair")
    print("----------------------------------------------")
    try:
        escolha = int(input("escolha: "))
        match escolha:
            case 1:
                try:
                    n = input("nome do item: ")
                    p = float(input("preço do item: "))
                    item = Item(n, p)
                    carrinhoDeCompras[len(carrinhoDeCompras)] = Item(n, p)
                    print(f"{item.nome} foi adicionado ao carrinho de compras!")
                except:
                    print(f"Houve um erro e o item {n} não foi adicionado.")
            case 2:
                try:
                    item = int(input("escolha o item que deseja remover: "))
                    carrinhoDeCompras.pop(item)
                except ValueError:
                    print("ValueError: Digite um valor válido")
                except KeyError:
                    print(f"Não foi possível remover o item {item} pois ele não existe.")
            case 3:
                try:
                    item = int(input("qual item você deseja alterar? "))
                    if item in carrinhoDeCompras:
                        print(f"item {item} selecionado!")
                        escolha = input("você deseja mudar o nome ou o preço? ")
                        if escolha == "nome":
                            nome = input("novo nome: ")
                            carrinhoDeCompras[item].nome = nome
                            print(f"o nome do item foi alterado para {nome} com sucesso!")
                        elif escolha == "preco":
                            try:
                                preco = float(input("novo preço: "))
                                carrinhoDeCompras[item].preco = preco
                                print(f"o preço do item foi alterado para {preco} com sucesso!")
                            except Exception as E:
                                print(f"{E} Não foi possível alterar o preço do item")
                        else:
                            print("não foi possível alterar este dado pois ele não existe")
                    else:
                        print("Este item não existe")
                except ValueError:
                    print(f"ValueError: Digite um valor válido")
            case 4:
                print(carrinhoDeCompras)

            case 5:
                break

            case _:
                print("escolha uma opção válida")
    except:
        print("ValueError: Digite um valor válido")

