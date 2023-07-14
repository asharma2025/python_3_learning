# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Get force function
def get_force(mass, acceleration):
  return mass * acceleration

# Calling get force with defined variables
train_force = get_force(train_mass, train_acceleration)

# print train force
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Get energy function
def get_energy(mass, c = 3*10**8):
  return mass * c**2

# Calling get energy with bomb mass
bomb_energy = get_energy(bomb_mass)

# Final function get work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

# Create variable for get work result
train_work = get_work(train_mass, train_acceleration, train_distance)

# Print results of get work 
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# Print bomb energy
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Write your code below: 
# F to C function
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 

# 100 F to C function call
f100_in_celsius = f_to_c(100)

# C to F function
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# 0 C to F function call
c0_in_fahrenheit = c_to_f(0)

