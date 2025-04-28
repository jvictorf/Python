#%%
lista_compra = []

while True:
    incluir_item = input("Entre com um item (ou digite 'remover' para excluir um item): ")
    
    if incluir_item == "":
        print("Lista final:", lista_compra)
        break
    elif incluir_item.lower() == "remover":
        item_remover = input("Digite o nome do item que deseja remover: ")
        if item_remover in lista_compra:
            lista_compra.remove(item_remover)
            print(f"Item '{item_remover}' removido.")
        else:
            print(f"Item '{item_remover}' não encontrado na lista.")
    else:
        lista_compra.append(incluir_item)
        print("Item adicionado:", incluir_item)
    
    print("Lista atual:", lista_compra)
