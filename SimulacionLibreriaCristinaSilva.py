import cnyt as lc
import unittest
import math

class TestlibrarycMethods(unittest.TestCase):

    def test_suma(self):
        suma = lc.suma((-2, 1), (1, 2))
        self.assertAlmostEqual(suma[0], -1)
        self.assertAlmostEqual(suma[1], 3)

        suma2 = lc.suma((3, -1), (4, 5))
        self.assertAlmostEqual(suma2[0], 7)
        self.assertAlmostEqual(suma2[1], 4)

    def test_producto(self):
        producto = lc.producto((-2, 1), (1, 2))
        self.assertAlmostEqual(producto[0], -4)
        self.assertAlmostEqual(producto[1], -3)

        producto2 = lc.producto((3, -1), (4, 5))
        self.assertAlmostEqual(producto2[0], 17)
        self.assertAlmostEqual(producto2[1], 11)

    def test_resta(self):
        resta = lc.resta((-2, 1), (1, 2))
        self.assertAlmostEqual(resta[0], -3)
        self.assertAlmostEqual(resta[1], -1)

        resta2 = lc.resta((3, -1), (4, 5))
        self.assertAlmostEqual(resta2[0], -1)
        self.assertAlmostEqual(resta2[1], -6)

    def test_division(self):
        division = lc.division((-2, 1), (1, 2))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], 1)

        division2 = lc.division((3, -1), (4, 5))
        self.assertAlmostEqual(division2[0], 0.17073170731707318)
        self.assertAlmostEqual(division2[1], -0.4634146341463415)

    def test_modulo1(self):
        modulo = lc.modulo1((-2, 1))
        self.assertAlmostEqual(modulo, 2.23606797749979)

        modulo2 = lc.modulo1((3, -1))
        self.assertAlmostEqual(modulo2, 3.1622776601683795)

    def test_conjugado(self):
        conjugado = lc.conjugado((-2, 1))
        self.assertEqual(conjugado, (-2, -1))

        conjugado2 = lc.conjugado((3, -1))
        self.assertEqual(conjugado2, (3, 1))

    def test_polarAcartesiano(self):
        polar1 = lc.polarAcartesiano((2, math.pi/4))
        self.assertAlmostEqual(polar1[0], 1.4142135623730951)
        self.assertAlmostEqual(polar1[1], 1.414213562373095)

        polar2 = lc.polarAcartesiano((5, math.pi/3))
        self.assertAlmostEqual(polar2[0], 2.5000000000000004)
        self.assertAlmostEqual(polar2[1], 4.330127018922194)

    def test_cartesianoApolar(self):
        polar1 = lc.cartesianoApolar((-2, 1))
        self.assertAlmostEqual(polar1[0], 2.23606797749979)
        self.assertAlmostEqual(polar1[1], math.atan(1 / -2))

        polar2 = lc.cartesianoApolar((3, -1))
        self.assertAlmostEqual(polar2[0], 3.1622776601683795)
        self.assertAlmostEqual(polar2[1], math.atan(-1 / 3))

    def test_fase(self):
        fase1 = lc.fase((-2, 1))
        self.assertAlmostEqual(fase1, math.atan(1 / -2))

        fase2 = lc.fase((3, -1))
        self.assertAlmostEqual(fase2, math.atan(-1 / 3))

print()
# Definir amplitudes complejas para las rendijas
# Amplitud al pasar por la rendija 1 (en forma polar)
amplitud_rendija1 = lc.polarAcartesiano((1 / math.sqrt(2), 0))  # Amplitud de 1/sqrt(2) con fase 0

# Amplitud al pasar por la rendija 2 (en forma polar)
amplitud_rendija2 = lc.polarAcartesiano((1 / math.sqrt(2), math.pi))  # Amplitud de 1/sqrt(2) con fase pi

# Sumar las amplitudes para obtener la interferencia
amplitud_total = lc.suma(amplitud_rendija1, amplitud_rendija2)

# Calcular la probabilidad total detectada (módulo al cuadrado de la amplitud total)
probabilidad_total = lc.modulo1(amplitud_total) ** 2

print(f"La probabilidad total detectada es: {probabilidad_total}")

if __name__ == '__main__':
    unittest.main()