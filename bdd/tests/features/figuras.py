class Figuras(object):
    def obtener_area_cuadrado(self, medida_lado):
        return medida_lado * medida_lado

    def obtener_area_rectangulo(self, base, altura):
        return base * altura

    def obtener_area_circulo(self, radio):
        return 3.1416 * radio ** 2

    def obtener_area_trapecio(self, base_menor, base_mayor, altura):
        return (base_mayor + base_menor) * altura / 2
