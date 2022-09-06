# Considering a carbon - epoxy plate with width and length of 0.3 m and 0.3 m, with a thickness of 0.001 m.
# This plate is under an axial force of 80 kN in direction of the fiber; and also it's under compression of 5 kN in perpendicular direction 
# to the fiber. 
# We need to determine the change on the dimensions on the plane of the plate, considering the following mechanical properties for the 
# carbon - epoxy system.

import numpy as np

E_1 = 187.25 # GPa
v_23 = v_32 = 0.467
G_23 = 3.72 # GPa

E_2 = E_3 = 25.84 # GPa
v_12 = v_21 = v_13 = v_31 = 0.278
G_12 = G_13 = 4.1 # GPa

# Forces
F_x = 80E3 # N
F_y = - 5E3 # N

# Dimensions
w = 0.3 # m
l = 0.3 # m
t = 0.001 # m

# Calculating the area of the plane
A = w * t

six_x = (F_x / A) / 1E9 # GPa
sig_y = (F_y / A) / 1E9 # GPa

S = np.array([[1 / E_1, (- v_21 / E_2), 0], [(- v_12 / E_1), 1 / E_2, 0], [0, 0, 1 / G_12]])
sig = np.array([[six_x], [sig_y], [0]])

epsilon = S.dot(sig)

dL_1 = epsilon[0] * l
dL_2 = epsilon[1] * w

l_f = l + dL_1 # m
w_f = w + dL_2 # m

print("The final length is: ", float(l_f,), " m. The final width is: ", float(w_f), " m.")