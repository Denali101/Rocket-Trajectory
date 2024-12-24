import math
G = 6.67*math.pow(10, -11)
MEarth = 5.97*math.pow(10, 24)
radius = 6.371*math.pow(10, 6)

def print_data(t, h, v, a, d):
    if h >= 0:
        print("Time: " + str(round(t, 2)) + "s")
        print("Altitude: " + str(round(h, 2)) + "m")
        print("Velocity: " + str(round(v, 2)) + "m/s")
        print("Acceleration: " + str(round(a, 2)) + "m/s^2")
        print("Drag: " + str(round(d, 2)))
        print("")


# Calculates temperature (h is altitude):
def temperature(h):
    if h < 11000:
        return 15.04 - 0.00649 * h
    elif 11000 < h < 25000:
        return -56.46
    elif h > 25000:
        return -131.21 + 0.00299 * h


# Calculates air pressure (h is altitude):
def air_pressure(h):
    if h < 11000:
        return 101.29 * math.pow((temperature(h) + 273.1) / 288.08, 5.256)
    elif 11000 < h < 25000:
        return 22.65 * math.exp(1.73 - 0.000157 * h)
    elif h > 25000:
        return 2.488 * math.pow((temperature(h) + 273.1) / 216.6, -11.388)


# Calculates the air density (h is altitude):
def air_density(h):
    return air_pressure(h) / (0.2869 * (temperature(h) + 273.1))

# Calculates gravity at an altitude
def gravity(h):
    g = G*MEarth / math.pow(radius+h,2)
    return g
