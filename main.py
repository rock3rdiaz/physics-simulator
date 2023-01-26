from vectors import Custom2DVector
from particles import ElectricParticle
from render import draw_electrical_field_lines


if __name__ == '__main__':
    print('running ...')

    v1 = Custom2DVector(4, 0)
    #v2 = Custom2DVector(0, 3)

    #print(f'---- sub: {v1 - v2}')
    #print(f'---- v1.norm(): {v1.norm()}')
    #print(f'---- v2.norm(): {v2.norm()}')
    #print(f'---- mul: {v1 * 5.0}')
    #print(f'---- div: {v1 / 5.0}')

    p1 = ElectricParticle(3e-3, v1)
    #print(p1.v_electrical_field(v2))

    draw_electrical_field_lines(p1)

    print('closing ...')
