import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

# Define the parametric equation
def r(t):
    x = 3.75 * np.sin(2*t) / t
    y = 3.75 * np.sin(t)**2
    z = 3.75 * np.sin(t)

    # Handle division by zero when t = 0
    x[t == 0] = 3.75

    return x, y, z

# Generate the data for the plot
t = np.linspace(0, 2*np.pi, 200)
x, y, z = r(t)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the parametric curve
ax.plot(x, y, z)

# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Set the title
ax.set_title('Parametric Curve')

# Show the plot
plt.show()
