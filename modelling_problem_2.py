#Write a function to calculate the pressure drop in a pipe given the flow velocity, density, viscosity, and pipe diameter,
#and pipe length, assuming the Reynold’s number is less than 2300. 

#Re < 2300: Laminar flow

def pressure_calc(velocity,density,viscosity,diameter,length):

    pressure_drop = 32 * viscosity *  length * velocity / diameter**2
    
    return pressure_drop