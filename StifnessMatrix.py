# This function calculates stifness matrix

def stifness_matrix(EF, c):

    k2 = [[EF, -EF],
          [-EF, EF]]
    k3 = k2
    k4 = k2
    k1 = [[c, -c],
          [-c, c]]
    k5 = k1

    print("K1:", k1)
    print("K2:", k2)
    print("K3:", k3)
    print("K4:", k4)
    print("K5:", k5)

    # Stifness matrix of the whole system

    k = [[k1[0][0], k1[0][1],          0,                 0,                 0,                 0],
         [k1[1][0], k1[1][1]+k2[0][0], k2[0][1],          0,                 0,                 0],
         [0,        k2[1][0],          k2[1][1]+k3[0][0], k3[0][1],          0,                 0],
         [0,        0,                 k3[1][0],          k3[1][1]+k4[0][0], 0,                 0],
         [0,        0,                 0,                 k4[1][0],          k4[1][1]+k5[0][0], 0],
         [0,        0,                 0,                 0,                 k5[1][0],          k5[1][1]]]

    return k
