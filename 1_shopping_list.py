def shopping_list() -> None:

    shopping_list = ["Botella de Ron", "Botella de vodka", "Huevos", "Jugo de naranja", "Jugo de Cranberry"]
    print("Lista de compras: ") 
    for product in shopping_list:
        print(product) 
    add_product = input("Agrega un producto a la lista de compras: ")
    shopping_list.append(add_product) 
    print("\nLista actualizada:")
    for product in shopping_list:
        print(product)

shopping_list()