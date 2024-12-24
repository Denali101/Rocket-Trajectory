import math
import functions
import seaborn as sns
import matplotlib.pyplot as plt

# Setting variables and constants
PI = math.pi
G = 6.67*math.pow(10, -11)
MEarth = 5.97*math.pow(10, 24)
radius = 6.371*math.pow(10, 6)

mBody = float(input("How heavy is the rocket without propellants? (kg) "))  # Kg
while (mBody<=0):
    print("Zander you dimwit")
    mBody = float(input("How heavy is the rocket without propellants? (kg) "))
mFuel = float(input("How heavy is the fuel? (kg) "))  # Kg
while (mFuel<=0):
    print("Zander you dimwit")
    mFuel = float(input("How heavy is the fuel? (kg) "))

tFlow = float(input("How long will the engines fire? (s) "))  # Kg/s
while (tFlow<=0):
    tFlow = float(input("How long will the engines fire? (s) "))
vFlow = mFuel / tFlow


# choosing the type of fuel
fuelVelocity = 0
print("Which fuel type would you like to use?")
print("   1. Methane")
print("   2. Jet Fuel (kerosene)")
print("   3. Hydrolox")
print("   4. Ammonium nitrate composite")
choice = 0
while (choice < 1 or choice > 4):
    choice = int(input("-> "))
if (choice == 1):
    fuelVelocity = 3034  # m/s
if (choice == 2):
    fuelVelocity = 2941  # m/s
if (choice == 3):
    fuelVelocity = 3816  # m/s
if (choice == 4):
    fuelVelocity = 2100  # m/s

mTotal = mBody + mFuel
mCurrent = mTotal
g = 9.81
time = 0
timeIncrement = 0.05  # seconds
# Radius of rocket
rRocket = float(input("Enter the radius of the rocket in m: "))
areaRocket = PI * rRocket ** 2
# Calculating DragCoefficient which is 1/2*A*C
dragCoefficient = 0.5 * areaRocket * 0.75
drag = 0
altitude = 0
v = 0
a = 0
x = []
y = []
d = []

# Drogue chute
drogue = False
drogueArea = 0
temporary = 0
temporary = input(str("Is there a drogue chute? (y/n): "))
while (temporary <= 0 or temporary > 40) {
    temporary = input(str("Is there a drogue chute? (y/n): "))
}
if temporary == "y":
    drogue = True
    drogueArea = PI * math.pow(float(input("Enter the radius of the drogue chute in meters: ")), 2)

# Height of parachute deployment on the way down
paraH = int(input("Enter the height at which the parachute deploys: "))
apogee = 0
paraArea = PI * math.pow(float(input("Enter the radius of the parachute in meters: ")), 2)

# POWERED ASCENT
while (mFuel > 0 and v >= 0 and orbit == False):
    v += a * timeIncrement - drag * timeIncrement
    drag = (v * v * dragCoefficient * functions.air_density(altitude)) / mCurrent
    a = fuelVelocity * vFlow / mCurrent - g
    altitude += v * timeIncrement
    time += timeIncrement

    #functions.print_data(time, altitude, v, a, drag)
    y.append(round(altitude, 2))
    x.append(round(time, 2))
    d.append(round(drag, 2))
    mFuel -= vFlow * timeIncrement
    mCurrent = mBody + mFuel

print("FUEL HAS RUN OUT" + "\n")
a = -1 * g  # Acceleration is now constant

# Case 1: Rocket returns to Earth
if (orbit == False):
  # UNPOWERED ASCENT
  while (v >= 0):
      functions.print_data(time, altitude, v, a, drag)
      y.append(round(altitude, 2))
      x.append(round(time, 2))
      d.append(round(drag, 2))
  
      drag = v * v * dragCoefficient * functions.air_density(altitude) / mCurrent
      v += a * timeIncrement - drag * timeIncrement
      altitude += v * timeIncrement
      time += timeIncrement
  
  print("Apogee reached")
  apogee = altitude
  
  # increasing drag coefficient if drogue chute
  if (drogue == True):
      print("Drogue chute is open")
      # increasing drag. Coef = 1/2*A*C
      dragCoefficient += 1 / 2 * drogueArea * 1.75
  
  a = -1 * g
  # FREE FALLING DESCENT
  while (altitude > paraH):
      functions.print_data(time, altitude, v, a, drag)
      y.append(round(altitude, 2))
      x.append(round(time, 2))
      d.append(round(drag, 2))
      drag = v * v * dragCoefficient * functions.air_density(altitude) / mCurrent
      v += a * timeIncrement + drag * timeIncrement
      altitude += v * timeIncrement
      time += timeIncrement
  
  # PARACHUTE DESCENT
  dragCoefficient += 1 / 2 * paraArea * 1.75
  print("Parachute deployed")
  while (altitude > 0):
      functions.print_data(time, altitude, v, a, drag)
      y.append(round(altitude, 2))
      x.append(round(time, 2))
      d.append(round(drag, 2))
      drag = v * v * dragCoefficient * functions.air_density(altitude) / mCurrent
      v += a * timeIncrement + drag * timeIncrement
      altitude += v * timeIncrement
      time += timeIncrement
  
  if y[-1] < 0:
      y[-1] = 0

sns.set_theme()
plt.figure()
plt.plot(x, y)  # Plot some data on the axes.
plt.xlabel('Time')
plt.ylabel('Altitude')
plt.title("Altitude vs. Time")

plt.show()

plt.plot(x, d)
plt.xlabel('Time')
plt.ylabel('Drag')
plt.title("Drag vs. Time")

plt.show()
