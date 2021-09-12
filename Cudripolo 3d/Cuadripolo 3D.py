from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#cuadripolo 3d

#comportemiento geometrico dipolo   a = 1
phi = np.arange(0, np.pi, 0.1)
tetha = np.arange(0, 2*np.pi, 0.1)
r1 = np.abs(np.sin(phi))*(np.abs(np.cos(phi))**(1/2))

#Guardar datos
z1 = np.array([phi, tetha, r1])
np.savetxt('datos cuadripolo 3d.csv', z1, fmt='%s')

tetha, phi = np.meshgrid(tetha, phi)     #devuelve matrices de coordenadas
r = np.abs(np.sin(phi))*(np.abs(np.cos(phi))**(1/2))

x = r * np.sin(phi) * np.cos(tetha)
y = r * np.sin(phi) * np.sin(tetha)
z = r * np.cos(phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z)
plt.title("Cuadripolo 3d")
plt.show()