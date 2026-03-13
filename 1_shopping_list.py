def shopping_list() -> None:

    shopping_list = ["Botella de whisky", "Botella de vodka", "Huevos", "Jugo de naranja", "Jugo de Cranberry"]
    print("Lista de compras: ") 
    for product in shopping_list:
        print(product) 

    add_product = input("Agrega un producto a la lista de compras: ")

    shopping_list.append(add_product) 

    print("\nLista actualizada:")

    for product in shopping_list:
        print(product) 

    product_remove = input("\nProducto que quieres eliminar de la lista: ")

    shopping_list.remove(product_remove)

    print("\nLista actualizada:")

    for product in shopping_list:
        print(product)

    search_product = input("\nEscribe el nombre del producto que quieres buscar en la lista de compras: ") 

    if search_product in shopping_list:
        print(f"Este es el producto que buscabas: {search_product}") 
    else: 
        print("No encuentro ese producto")


shopping_list()