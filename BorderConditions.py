# Including border conditions

def border_conditions(k):
    k[0][0] = 1
    for i in range(1, len(k[0])):
        k[0][i] = 0

    for i in range(1, len(k)):
        k[i][0] = 0

    for i in range(0, 5):
        k[5][i] = 0
    for i in range(0, 5):
        k[i][5] = 0
    k[5][5] = 1

    return k
