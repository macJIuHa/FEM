# This is the body of FEM program

# Including important modules

from InputFEM import initial_data
from StifnessMatrix import stifness_matrix
from BorderConditions import border_conditions
from matan import inverse_matrix
import first_node_mov
import second_node_mov
import third_node_mov
import fourth_node_mov
import fifth_node_mov
import first_node_force
import second_node_force
import third_node_force
import fourth_node_force
import fifth_node_force

# Function that gets initial data

EF, f, c = initial_data()

# Function that calculates stifness matrix

k = stifness_matrix(EF, c)
print("Матрица жесткости до введения ГУ:")
print("K:", k)


# Including border conditions

k = border_conditions(k)
print("Матрица жесткости после введения ГУ:")
print("K:", k)

# Define the FORCE vector

force = [0, 0, f, 0, -2 * f, 0]
print("Вектор сил:", force)

invk = inverse_matrix(k)
print("Обратная матрица:")
print("K:", k)

q = []
for i in range(len(force)):
    u = 0
    for j in range(len(force)):
        u += invk[i][j] * force[j]
    q.append(u)
print('U', q)

# Calculate approximations
first_node_mov.mov(q[4], q[1])
second_node_mov.mov(q[0], q[1])
third_node_mov.mov(q[1], q[2])
fourth_node_mov.mov(q[2], q[3])
fifth_node_mov.mov(q[2], q[5])

# Calculate force in the kernel
first_node_force.force(q[4], q[1], c)
second_node_force.force(q[0], q[1], EF)
third_node_force.force(q[1], q[2], EF)
fourth_node_force.force(q[2], q[3], EF)
fifth_node_force.force(q[2], q[5], c)
