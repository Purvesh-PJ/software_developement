import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a 3D vector (point in space)
vector = np.array([2, 3, 4])  # (x, y, z)

# Define a 3D rotation matrix for 90-degree rotation around the Z-axis
theta = np.radians(90)  # Convert degrees to radians
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]  # Z-axis remains unchanged
])

# Apply rotation (Matrix multiplication)
rotated_vector = np.dot(rotation_matrix, vector)

# Print results
print("Original vector:", vector)
print("Rotated vector:", rotated_vector)

# Plotting for visualization
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Plot original vector
ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='r', label="Original Vector")

# Plot rotated vector
ax.quiver(0, 0, 0, rotated_vector[0], rotated_vector[1], rotated_vector[2], color='b', label="Rotated Vector")

# Labels and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
ax.set_title("3D Vector Rotation Around Z-Axis")
plt.show()
