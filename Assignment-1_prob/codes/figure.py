import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the triangle
vertices = np.array([[0, 0], [4, 0], [2, 3]])

# Calculate the angle bisector for the first vertex (vertex A)
def calculate_angle_bisector(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    angle_bisector = v1 / np.linalg.norm(v1) + v2 / np.linalg.norm(v2)
    return angle_bisector / np.linalg.norm(angle_bisector)

angle_bisector = calculate_angle_bisector(vertices[0], vertices[1], vertices[2])

# Plot the triangle and angle bisector
plt.figure()
plt.plot(vertices[:, 0], vertices[:, 1], 'bo-')  # Plot triangle vertices
plt.quiver(vertices[0, 0], vertices[0, 1], angle_bisector[0], angle_bisector[1], color='r', angles='xy', scale_units='xy', scale=1, label='Angle Bisector')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle with Angle Bisector')
plt.grid()
plt.legend()
plt.axis('equal')
plt.show()

