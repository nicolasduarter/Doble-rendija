import numpy as np
import matplotlib.pyplot as plt

# Parámetros
wavelength = 500e-9  # Longitud de onda (500 nm)
d = 0.1e-3          # Separación entre las rendijas (0.1 mm)
L = 1               # Distancia de las rendijas a la pantalla (1 m)
screen_points = 100000  # Número de puntos en la pantalla

# Generar puntos en la pantalla
x = np.linspace(-0.05, 0.05, screen_points)  # 5 cm a cada lado de la rendija

# Cálculo del patrón de interferencia
# El ángulo de difracción
theta = np.arcsin(x / L)
# Intensidad del patrón de interferencia
I = (np.cos(np.pi * d * np.sin(theta) / wavelength))**2

# Normalizar la intensidad
I_normalized = I / np.max(I)

# Graficar el patrón de interferencia
plt.figure(figsize=(10, 6))
plt.plot(x, I_normalized, color='blue')
plt.title('Patrón de Interferencia del Experimento de Doble Rendija')
plt.xlabel('Posición en la pantalla (m)')
plt.ylabel('Intensidad Normalizada')
plt.grid()
plt.show()