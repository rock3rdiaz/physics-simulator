from vectors import Custom2DVector
from particles import ElectricParticle
from render import draw_electrical_field_lines


def punto1():
    v1 = Custom2DVector(4, 0)
    v2 = Custom2DVector(-1, 3)
    p1 = ElectricParticle(3e-3, v1)
    
    print(p1.v_electrical_field(v2))

    draw_electrical_field_lines(p1)
    
def punto2():
    # cargas
    v1 = Custom2DVector(0, 0)
    v2 = Custom2DVector(0, 1)
    v3 = Custom2DVector(1, 1)
    v4 = Custom2DVector(1, 0)
    
    # particula de prueba
    prueba = Custom2DVector(5, 5)
    
    p1 = ElectricParticle(1.602e-19, v1)
    p2 = ElectricParticle(-1.602e-19, v2)
    p3 = ElectricParticle(1.602e-19, v3)
    p4 = ElectricParticle(-1.602e-19, v4)
    
    campo_electrico = p1.v_electrical_field(prueba) + p2.v_electrical_field(prueba) + p3.v_electrical_field(prueba) + p4.v_electrical_field(prueba)
    print(f'----- el campo electrico generado por las cargas es de {campo_electrico}')

    #draw_electrical_field_lines(p1)
    
if __name__ == '__main__':
    print('running ...')

    punto2()

    print('closing ...')
