from math import *
import csv

w = 2*pi*60

def Z(C):
    numerator = (30 + 81.81j)*(-1j/(w*C))
    denumonator = (30 + 81.81j) + (-1j/(w*C))
    return numerator/denumonator

if __name__ == '__main__':
    power_factors = [0.45, 0.55, 0.67, 0.87, 1.00, 0.92, 0.65, 0.48, 0.37]
    for C in range(1, floor(40/5)+1):
        C_value = C * 5 * 1e-6  # Convert microfarads to farads
        impedance = Z(C_value)
        theta = atan2(impedance.imag, impedance.real)
        pf = cos(theta)
        print(f"C: {C*5}uF, calculated pf: {round(pf,2)}, measured pf: {power_factors[C]}, error: {round(100*abs(pf - power_factors[C])/power_factors[C], 3)}%")
    