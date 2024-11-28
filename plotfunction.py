import numpy as np
import math
import matplotlib.pyplot as plt

# Define the function
def calculate_plastic_waste(T, P, T_opt=160, P_opt=60, a=0.001, b=0.01, W_min=5):
    """
    Calculate plastic waste based on deviations from optimal temperature and pressure.
    
    Args:
        T (float): Temperature.
        P (float): Pressure.
        T_opt (float): Optimal temperature where waste is minimal.
        P_opt (float): Optimal pressure where waste is minimal.
        a (float): Weight for temperature deviation.
        b (float): Weight for pressure deviation.
        W_min (float): Minimum waste percentage.
    
    Returns:
        float: Plastic waste percentage.
    """
    # Calculate squared deviations
    temp_deviation = a * (T - T_opt) ** 2
    press_deviation = b * (P - P_opt) ** 2

    # Combine deviations and add the minimum waste
    W = W_min + temp_deviation + press_deviation
    return W  # Round to 2 decimal places

# Generate T and P values
T = np.linspace(0, 400, 50)  # Temperature range
P = np.linspace(0, 100, 50)   # Pressure range
T, P = np.meshgrid(T, P)      # Create a grid for 3D plotting

# Calculate W values
W = calculate_plastic_waste(T, P)

# Plot the function
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(T, P, W, cmap='viridis')

# Add labels and title
ax.set_xlabel('Temperature (T)')
ax.set_ylabel('Pressure (P)')
ax.set_zlabel('Plastic Waste (W)')
ax.set_title('Plastic Waste as a Function of Temperature and Pressure')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()