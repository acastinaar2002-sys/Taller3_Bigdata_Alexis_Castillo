def show_inventory(inventory):
    for item in inventory:
        print(item)

inventory_list = ["Glock 9", "Chaleco", "Botiquin", "Balas", "Mini uzi"]
print("Que tienes en la maleta:")
show_inventory(inventory_list)


search_inventory = input("\nEscribe lo que buscas en la maleta: ") 

if search_inventory in inventory_list:
        print(f"Este es esto lo que buscabas: {search_inventory}") 
else: 
        print("No encuentro eso")

remove_inventory = input("Que quieres eliminar de la maleta: ") 
inventory_list.remove(remove_inventory) 
print("\nLa Maleta tienes mas espacio:", inventory_list)


show_inventory(inventory_list)