def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

grades_list = [90, 80, 71, 45, 100]
average = calculate_average(grades_list)
print("Promedio de notas: ", average)