import matplotlib.pyplot as plt
import numpy as np

# Datos fijos conocidos del nuevo experimento
K = 10000
N_0 = 500
t_fijo = 1.0  # El dato experimental fue tomado exactamente a la 1 hora


# Definimos la función logística donde la variable que cambia y queremos probar es 'r'
def N_segun_r(r_variable):
    return K / (1 + ((K / N_0) - 1) * np.exp(-r_variable * t_fijo))


# Rangos de tasas intrínsecas a explorar en el gráfico (por ejemplo, desde r=0.1 hasta r=3.0)
N_points = 100
r_inicial = 0.1
r_final = 3.0
values_of_r = np.linspace(r_inicial, r_final, N_points)
values_of_N = N_segun_r(values_of_r)

# Ajuste manual e inspección numérica por aproximaciones consecutivas (método solicitado):
# Vamos probando valores de r para ver cuál nos acerca a las 3000 células estimadas.
r = 1.0
print(f"Para r={r:.2f}, la población en t=1 es N={N_segun_r(r):.1f}")
r = 1.5
print(f"Para r={r:.2f}, la población en t=1 es N={N_segun_r(r):.1f}")
r = 2.0
print(f"Para r={r:.2f}, la población en t=1 es N={N_segun_r(r):.1f}")

# Estrechamos el cerco analizando la salida en consola para llegar al valor real
r = 2.09
print(f"Para r={r:.3f}, la población en t=1 es N={N_segun_r(r):.1f}")
r = 2.094
print(f"Para r={r:.3f}, la población en t=1 es N={N_segun_r(r):.1f}")
r = 2.0972
print(f"Para r={r:.6f}, la población en t=1 es N={N_segun_r(r):.1f}")

fig, gfx = plt.subplots()
gfx.set_xlabel("$r$ (Tasa intrínseca)")  # Ahora el eje X representa la tasa r
gfx.set_ylabel("Población a t=1 hora")

# Grafica la población resultante en t=1 para cada valor de tasa r
gfx.plot(values_of_r, values_of_N, color="purple", label="N(r) en t=1")
# Línea horizontal que representa nuestro dato real de laboratorio (3000 células)
gfx.plot(values_of_r, 0 * values_of_r + 3000, color="green", label="Dato Real (3000)")
gfx.legend()
plt.savefig("calibracion_r.png")
plt.show()