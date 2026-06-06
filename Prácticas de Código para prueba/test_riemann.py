import numpy as np
import matplotlib.pyplot as plt

lower_limit = 0
upper_limit = 1
rectangles = 100

def f(x):
    return 3 * (x**2)

print("System ready for Reimann Sums")

delta_x = (upper_limit - lower_limit) / rectangles
total_area = 0
for i in range(1, rectangles + 1):
    current_x = lower_limit + (i - 0.5) * delta_x
    total_area += f(current_x) * delta_x

exact_value = 1
error_absolute = abs(exact_value - total_area)

print(f"Estimated area: {total_area}")
print(f"Exact area: {exact_value}")
print(f"Absolute error: {error_absolute}")


x_curve = np.linspace(lower_limit, upper_limit, 100)
y_curve = f(x_curve)

plt.figure(figsize=(8, 6))
plt.plot(x_curve, y_curve, 'r-', label='f(x) = 3x^2', lw=2)

x_rects = np.linspace(lower_limit + delta_x/2, upper_limit - delta_x/2, rectangles)
y_rects = f(x_rects)

plt.bar(x_rects, y_rects, width=delta_x, alpha=0.3,
        color='blue', edgecolor='black', label='Riemann Sum (Midpoint)')

plt.title(f'Riemann Sum with {rectangles} Rectangles')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
