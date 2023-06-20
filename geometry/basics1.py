import numpy as np
import matplotlib.pyplot as plt

# 2D points(pixel coordinates in an image) can be denoted using a pair of values (x,y)
# Where x is the horizontal position and y is the vertical position

# Define Coordinates
x = 3
y = 2

# Create a scatter plot with the points
plt.scatter(x, y)

# Add a title and labels for the x and y axes
# plt.title('Plotting a Point')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')

# Show the plot
# plt.show()

# A homogeneous coordinate is a vector with one additional component compared to its Cartesian coordinate representation
# in homogeneous coordinates, a 2d point is represented by (x, y, w), where w is a scaling factor
# can be non-zero but always set to 1
# note: A homogeneous vector can be converted back to inhomogeneous by dividing through by the last element(w)
x = 4
y = 6
w = 1
# represents the point in homogeneous point
p = np.array([x, y, w])
# Convert homogeneous coordinates to Cartesian coordinates
cartesian_coords = p[:2] / p[2]
# print("Cartesian coordinates:", cartesian_coords)

# In homogeneous coordinates, a 2D line can be represented as a 3-component vector (a, b, c), where
# a, b, and c are the coefficients of the line equation ax + by + c = 0.
# Define the line's equation coefficients
a = -2
b = 1
c = -1

# Represent the line in homogeneous coordinates
line = np.array([a, b, c])

# print("Homogeneous coordinates:", line)

# When using homogeneous coordinates, we can compute the intersection of two lines as
# x˜ = ˜l1 × ˜l2, where × is the cross product operator
# Define two lines represented by their homogeneous coordinates
line1 = np.array([1, 2, -4])
line2 = np.array([2, -1, 3])

# Compute the intersection point in homogeneous coordinates
cross_product = np.cross(line1, line2)
intersection = cross_product / cross_product[2]
# Define a range of values for the x-axis
x = np.linspace(-10, 10, 100)

# Plot the lines
plt.plot(x, (-line1[0] * x - line1[2]) / line1[1], label='Line 1')
plt.plot(x, (-line2[0] * x - line2[2]) / line2[1], label='Line 2')

# Plot the intersection point
plt.plot(intersection[0], intersection[1], 'ro', label='Intersection')

# Add labels and legend to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

if __name__ == '__main__':
    print()