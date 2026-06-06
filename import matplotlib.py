import matplotlib.pyplot as plt
import numpy as np

# --- Bloque Original del Profesor ---
r = 0.4
K = 10000
N_0 = 500


def N(t):
    return K / (1 + ((K / N_0) - 1) * np.exp(-r * t))


N_points = 100
t_inicial = 0
t_final = 12
values_of_t = np.linspace(t_inicial, t_final, N_points)
values_of_N = N(values_of_t)

# --- NUEVA AUTOMATIZACIÓN PARA RESOLVER LA P2 DIRECTAMENTE ---
# Usamos un método numérico de paso fino (búsqueda incremental)
t_busqueda = 0.0  # Comenzamos desde el tiempo cero
paso = 0.001  # El tamaño del paso determina la precisión (0.001 da 3 decimales de precisión)
poblacion_objetivo = 8000.0

# El código evaluará la función N(t) y avanzará en el tiempo mientras no alcance los 8000
while N(t_busqueda) < poblacion_objetivo:
    t_busqueda += paso  # Incrementa el tiempo en un paso muy pequeño

# Al salir del bucle, habremos encontrado el instante preciso
print(
    f"El valor exacto de t cuando N(t)={poblacion_objetivo} es: {t_busqueda:.3f} horas")

print(f"Verificación: N({t_busqueda:.3f}) = {N(t_busqueda):.1f}")


fig, gfx = plt.subplots()
gfx.set_xlabel("$t$")
gfx.plot(values_of_t, values_of_N, color="purple", label="Logistic")

# MODIFICACIÓN EN EL GRÁFICO: Cambiamos la línea objetivo a 8000 para la P2
gfx.plot(values_of_t, 0 * values_of_t + 8000, color="green", label="Target (8000)")
gfx.legend()
plt.savefig("logistic.png")
plt.show()