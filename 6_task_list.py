tasks = []

def add_task():
    task = input("Ingrese tarea: ")
    tasks.append(task)

def show_tasks():
    for task in tasks:
        print(task)

def remove_task():
    task = input("Eliminar tarea: ")
    if task in tasks:
        tasks.remove(task)

def complete_task():
    task = input("Tarea completada: ")
    if task in tasks:
        tasks.remove(task)
        tasks.append("Completada: " + task)

def main():
    while True:
        option = input("1 agregar, 2 mostrar, 3 eliminar, 4 completar, 5 salir: ")

        if option == "1":
            add_task()
        elif option == "2":
            show_tasks()
        elif option == "3":
            remove_task()
        elif option == "4":
            complete_task()
        elif option == "5":
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

main()