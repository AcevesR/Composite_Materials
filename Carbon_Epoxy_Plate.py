import numpy as np
import matplotlib.pyplot as plt

# Considering a carbon - epoxy plate with the following mechanical properties for the fiber and the matrix.
# We need to graph E_1, E_2, v_12, v_21 and G_12, against V_f, using V_f [0, 1], with dV_f = 0.1. 

E_f = 250 #GPa
v_f = 0.4 
G_f = 8.32 #GPa

E_m = 5.8 #GPa
v_m = 0.38
G_m = 8.1 #GPa

dV_f = 0.1

V_f_i = 0

V_f_f = 1

V_f = np.linspace(V_f_i, V_f_f, int((V_f_f / dV_f) + 1))

V_m = 1 - V_f

E_1 = E_f * V_f + E_m * V_m

E_2 = 1 / ((V_f / E_f) + (V_m / E_m))

v_12 = v_f * V_f + v_m * V_m

v_21 = 1 / ((V_f / v_f) + (V_m / v_m))

G_12 = 1 / ((V_f / G_f) + (V_m / G_m))

# Graph method

fig = plt.figure()

grp_E = plt.subplot(211)
grp_v = plt.subplot(212)

grp_E.plot(V_f, E_1, label = '$E_1$')
grp_E.plot(V_f, E_2, label = '$E_2$')
grp_E.plot(V_f, G_12, label = '$G_{12}$')

grp_E.legend()
grp_E.set_xlabel('$V_f$')
grp_E.set_ylabel('$[GPa]$')

grp_v.plot(V_f, v_12, label = '$v_{12}$')
grp_v.plot(V_f, v_21, label = '$v_{21}$')

grp_v.legend()
grp_v.set_xlabel('$V_f$')
grp_v.set_ylabel('$[ / ]$')

plt.show()
