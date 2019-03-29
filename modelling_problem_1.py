#Given an incompressible fluid flowing through a short section of horizontal pipe, write a function to calculate
#the outlet pressure if the inlet pressure, inlet velocity, and outlet velocity are known

#all units are in metric
#assume incompressible fluid is water (density = 1000 kg/m^3)
#pressure is in Pa
#velocities are in m/s

def outlet_pressure(inlet_pressure,inlet_velocity,outlet_velocity):
    density = 1000 

    opressure = inlet_pressure + 0.5 * density * (inlet_velocity**2 - outlet_velocity**2)

    return opressure
