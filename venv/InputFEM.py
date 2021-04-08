# Function, that gets initial data

def initial_data():
    print("Введите необходимые значения:")
    EF = float(input("Жесткость элементов EF ="))
    F = float(input("Сила F ="))
    c = float(input("Жесткость пружины с ="))
    return EF, F, c