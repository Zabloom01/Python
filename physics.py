# Parameters:
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3.0*10**8 # speed of light

###########################
#### define functions:  ###
###########################
# Convert farenheit to celsius 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Convert celsius to farenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# "Use the force!"
def get_force(mass, acceleration):
  return mass * acceleration

# Energy function
def get_energy(mass, c):
  return mass * c

# Work function
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

###########################
#### Test functions:  #####
###########################

# Convert farenheit to celsius
f_100_in_celsius = f_to_c(100)
print("{:.2f}".format(f_100_in_celsius))

# Convert celsius to farenheit
c0_in_farenheit = c_to_f(0)
print("{:.2f}".format(c0_in_farenheit))

# Calculate force of train
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies {} Newtons of force".format(train_force))

# Test energy function
bomb_energy = get_energy(bomb_mass, c)
# Put in scientific notation and 2-decimals
print("A 1kg bomb supplies {} Joules.".format("{:.2e}".format(bomb_energy)))

# Calculate train work
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over Y meters".format("{:.2e}".format(train_work)))
