import math
import random
from vectors import Custom2DVector, Custom3DVector
from particles import ElectricParticle
from render import draw_electrical_field_lines, draw_electrical_particles_in_sphere


def punto1():
    v1 = Custom2DVector(4, 0)
    v2 = Custom2DVector(-1, 3)
    p1 = ElectricParticle(3e-3, v1)

    print(f'------ El campo electrico generado es {p1.v_electrical_field(v2)}')
    print(f'------ El potencial electrico generado es {p1.electrical_potential(v2.norm())} V')

    draw_electrical_field_lines(p1)


def punto2():
    # cargas
    v1 = Custom2DVector(0, 0)
    v2 = Custom2DVector(0, 1)
    v3 = Custom2DVector(1, 1)
    v4 = Custom2DVector(1, 0)

    # particula de prueba
    prueba = Custom2DVector(5, 5)

    p1 = ElectricParticle(-1.602e-19, v1)
    p2 = ElectricParticle(1.602e-19, v2)
    p3 = ElectricParticle(-1.602e-19, v3)
    p4 = ElectricParticle(1.602e-19, v4)

    campo_electrico = p1.v_electrical_field(prueba) + p2.v_electrical_field(prueba) + p3.v_electrical_field(
        prueba) + p4.v_electrical_field(prueba)
    print(f'----- el campo electrico generado por las cargas es de {campo_electrico}')


def punto4():
    # particula de prueba
    prueba = Custom3DVector(0.5, 1.5)

    # cargas
    cargas = []
    num_cargas = 5000
    ratio = 3.0  # radio de la esfera
    for e in range(1, num_cargas):
        x = round(random.uniform(-3.0, 3.0), 2)
        y = round(random.uniform(-3.0, 3.0), 2)
        try:
            z = math.sqrt((ratio ** 2) - (x ** 2) - (y ** 2))
        except ValueError:
            continue
        r1 = Custom3DVector(x, y, z)
        p1 = ElectricParticle(-1.602e-19, r1)
        cargas.append(p1)

        r2 = Custom3DVector(x, y, -1 * z)
        p2 = ElectricParticle(-1.602e-19, r2)
        cargas.append(p2)

    campos = [c.s_electrical_field(prueba.norm()) for c in cargas]

    draw_electrical_particles_in_sphere(cargas, ratio)

    print(f'----- el campo electrico generado por las {num_cargas} cargas es de {sum(campos)}')


if __name__ == '__main__':
    print('running ...')

    punto4()

    print('closing ...')
