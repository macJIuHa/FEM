# Calculates fifth node force

from Aproximation import force_approximation


def force(q1, q2, c):
    print()
    print("Усилия для пятого элемента (пружины):")
    print("0   ", force_approximation(0, [q1, q2], 1, c))
    print("0.25", force_approximation(0.25, [q1, q2], 1, c))
    print("0.5 ", force_approximation(0.5, [q1, q2], 1, c))
    print("0.75", force_approximation(0.75, [q1, q2], 1, c))
    print("1   ", force_approximation(1, [q1, q2], 1, c))
