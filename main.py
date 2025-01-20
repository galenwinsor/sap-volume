from sympy import *

x, z = symbols('x z')

init_printing(use_unicode=True)

water_height = float(input("Water height in inches: "))

a = 0.1745
b = 1.1439

tank_shape = a * b ** x

theta = 0.029296875

tank_length = 192

water_slope = -tan(theta) + water_height

x_bound = log(water_height/a)/log(b)

z_bound = min(water_height / tan(theta), tank_length)

area = 2 * integrate(water_slope - tank_shape, (x, 0, x_bound))

volume = integrate(area, (z, 0, z_bound))

print("Volume:", volume)
