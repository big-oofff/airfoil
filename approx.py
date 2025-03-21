import numpy as np
L = 15  
c_root = 5  
c_tip = 2  
def chord_length(x):
    return c_root * (1 - x / L) + c_tip * (x / L)
def z_top(x, y):
    c_x = chord_length(x)
    return c_x * (
        0.3 * np.sqrt(y / c_x)
        - 0.13 * (y / c_x)
        - 0.35 * (y / c_x)**2
        + 0.28 * (y / c_x)**3
        - 0.1 * (y / c_x)**4
        )
num_x = 1000  
num_y = 1000  
x_values = np.linspace(0, L, num_x)
surface_area = 0
for i in range(num_x - 1):
    x = x_values[i]
    x_next = x_values[i + 1]
    dx = x_next - x
    c_x = chord_length(x)
    y_values = np.linspace(0, c_x, num_y)
    for j in range(num_y - 1):
        y = y_values[j]
        y_next = y_values[j + 1]
        dy = y_next - y
        z_topleft = z_top(x, y)
        z_topright = z_top(x_next, y)
        z_bottomleft = z_top(x, y_next)
        z_bottomright = z_top(x_next, y_next)
        dz_dx = (z_topright - z_topleft) / dx
        dz_dy = (z_bottomleft - z_topleft) / dy
        dA = np.sqrt(1 + dz_dx**2 + dz_dy**2) * dx * dy
        surface_area += dA
print(f"Approximate surface area of the upper surface: {surface_area:.2f} square feet")
