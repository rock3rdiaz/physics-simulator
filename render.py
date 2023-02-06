from particles import ElectricParticle
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery-nogrid')


def draw_electrical_field_lines(p: ElectricParticle):
    """
    Dibuja las lineas del campo electrico generado por la 
    particula electrica p
    """
    
    x = np.linspace(-4, 4, 10)
    y = np.linspace(-4, 4, 10)
    X, Y = np.meshgrid(x, y)
    U = X
    V = Y

    # plot
    fig, ax = plt.subplots()

    #ax.scatter(x=[p.r.x], y=[p.r.y])
    ax.quiver(X, Y, U, V, color="C0", angles='xy',
              scale_units='xy', scale=5, width=.015)

    ax.set(xlim=(-5, 5), ylim=(-5, 5))

    plt.show()


def draw_electrical_particles_in_sphere(cargas: list, r: float):
    """
    Dibuja las particulas electricas
    @param cargas: Listado de cargas electricas
    @param r: Radio de la esfera
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    x = [c.r.x for c in cargas]
    y = [c.r.y for c in cargas]
    z = [c.r.z for c in cargas]

    ax1.scatter(x, y, z, c='g', marker='o')
    plt.show()
