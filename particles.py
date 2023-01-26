from vectors import Custom2DVector


class ElectricParticle:
    """
    Representa una carga electrica
    """
    def __init__(self, q: float, r: Custom2DVector = Custom2DVector(0, 0)):
        self.q = q
        self.r = r
        self.K= 9e9 # N*m^2/C^2

    def v_electrical_field(self, r: Custom2DVector) -> tuple:
        """
        Calcula el campo electrostatico generado por esta particula electrica
        en una posicion r.
        @param: q: carga puntual generadora del campo electrico
        @param r: coordenada en las que se desea medir la magnitud del campo generado
        @return: campo electrico generado
        """
        r_prime = r - self.r
        return r_prime * (self.K * (self.q / (r_prime.norm() ** 3)))

    def s_electrical_field(self, r: float) -> float:
        """
        Calcula el campo electrostatico generado por esta carga
        a una distancia r.
        @param r: distancia a la que se desea medir la magnitud del campo generado
        @return: magnitud del campo electrico generado
        """
        return self.K * (self.q / r ** 2)

    def electrical_potential(self, q: float, r: Custom2DVector) -> float:
        """
        Calcula el potencial electrico generado por una carga q
        a una distancia r. 
        @param: q: carga puntual generadora del potencial electrico
        @param r: distancia a la que se desea medir el potencial electrico
        @return: potencial electrico generado
        """
        return self.K * (q / r)
