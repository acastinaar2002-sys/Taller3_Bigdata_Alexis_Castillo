def search_student():

    students = ["Alex", "Maria", "John", "Sofia", "Carlos", "Emma"]

    name = input("Escribe el nombre del estudiante que buscas: ")

    if name in students:
      print("Estudiante encontrado")
    else:
      print("Estudiante no encontrado") 

search_student()