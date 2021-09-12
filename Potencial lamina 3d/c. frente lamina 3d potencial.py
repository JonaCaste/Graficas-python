from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection ='3d')

q = 2
d = 2
x = np.arange(0.1, np.pi, 0.1)
y = np.arange(0.1, 2*np.pi, 0.1)

x, y = np.meshgrid(x, y)
z = (q/x)-(q/((x**2)+(4*(d**2))-(4*x*d*np.cos(np.pi))))

z2= (q/2)-(q/((2**2)+(4*(d**2))-(4*2*d*np.cos(y))))


surf = ax.plot_surface(x, y, z, cmap='winter', cstride=2, rstride=2)
ax.set_title('Potencial carga puntual frente a lamina 3D (r variante)')
plt.draw()
surf2 = ax2.plot_surface(x, y, z2, cmap='winter', cstride=2, rstride=2)
ax2.set_title('Potencial carga puntual frente a lamina 3D (tetha variante)')
plt.draw()
plt.show()