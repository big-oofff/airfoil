import numpy as np
import matplotlib.pyplot as plt

# Define the chord length function
def c(x, c_root=5, c_tip=2, L=15):
    return c_root * (1 - x / L) + c_tip * (x / L)

# Define the upper and lower surface equations for the current design
def z_top_current(y, c_val):
    return -y * (y / c_val - 1)

def z_bot_current(y, c_val):
    return (y / 2) * (y / c_val - 1)

# Define x (spanwise location) for a specific cross-section
x_fixed = 0  # Root chord (x = 0)
c_val = c(x_fixed)  # Chord length at this location

# Generate chordwise positions (y)
y_vals = np.linspace(0, c_val, 300)
z_top_vals = z_top_current(y_vals, c_val)
z_bot_vals = z_bot_current(y_vals, c_val)

# Compute slopes (dz/dy)
dz_top_dy = np.gradient(z_top_vals, y_vals)
dz_bot_dy = np.gradient(z_bot_vals, y_vals)

# Generate velocity vectors (tangents to the surfaces)
v_y = np.ones_like(y_vals)  # Constant y-component
v_z_top = dz_top_dy  # Slope of the top surface
v_z_bot = dz_bot_dy  # Slope of the bottom surface

# Plot the cross-section
plt.figure(figsize=(10, 6))
plt.plot(y_vals, z_top_vals, label="Top Surface", color="blue")
plt.plot(y_vals, z_bot_vals, label="Bottom Surface", color="red")

# Add velocity vectors (quiver plot)
plt.quiver(y_vals[::20], z_top_vals[::20], v_y[::20], v_z_top[::20], 
           angles="xy", scale_units="xy", scale=10, color="blue", label="Velocity Vectors (Top)")
plt.quiver(y_vals[::20], z_bot_vals[::20], v_y[::20], v_z_bot[::20], 
           angles="xy", scale_units="xy", scale=10, color="red", label="Velocity Vectors (Bottom)")

# Add labels and formatting
plt.title(f"Cross-Section at x = {x_fixed} (Root Chord)")
plt.xlabel("Chordwise Position (y)")
plt.ylabel("Vertical Position (z)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()
plt.grid()
plt.show()
