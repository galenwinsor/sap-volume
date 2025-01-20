from sympy import *

# X represents the horizontal axis of the tank, Z the length
x, z = symbols('x z')

# The height of the water at the midpoint of the tank, where the sensor is
water_height = float(input("Water height in inches: "))

# Coefficents for tank shape
a = 0.1745
b = 1.1439

# Constants
water_angle_with_ground_radians = 0.029296875
tank_length_inches = 192
tank_width_inches = 30

# Approx of tank shape
tank_shape = a * b ** x

# Water height above floor of tank 
midpoint_water_height_at_given_z = water_height - tan(water_angle_with_ground_radians) * z

x_bound = min(log(water_height / a) / log(b), tank_width_inches)

z_bound = min(water_height / tan(water_angle_with_ground_radians), tank_length_inches)

area = 2 * integrate(midpoint_water_height_at_given_z - tank_shape, (x, 0, x_bound))

volume = integrate(area, (z, 0, z_bound))

print("Volume:", str(volume / 231) + " gallons")
