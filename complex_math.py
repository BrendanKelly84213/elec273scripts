# /home/brendan/Dev/complex_math.py

import cmath
import re
from math import *
import readline

# Override math functions to round results for small floating-point errors
def rounded(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if abs(result) < 1e-10:
            result = 0
        return result
    return wrapper

cos = rounded(cos)
sin = rounded(sin)
tan = rounded(tan)
exp = rounded(exp)
log = rounded(log)
sqrt = rounded(sqrt)



# Update the regex to support float phasor forms
def parse_phasor_notation(expression):
    def phasor_replacer(match):
        magnitude = float(match.group(1))
        angle = float(match.group(3))
        rect = phasor_to_rect(magnitude, angle)
        return f"({rect.real}+{rect.imag}j)"
    
    # Regex to match phasor notation (e.g., 1@90)

    phasor_pattern = r"(\d+(\.\d+)?)[@](-?\d+(\.\d+)?)"
    return re.sub(phasor_pattern, phasor_replacer, expression)

# Modify the complex_math function to handle phasor notation
def complex_math(expression):
    try:
        # Parse and replace phasor notation
        expression = parse_phasor_notation(expression)
        # Evaluate the expression
        
        expression = expression.replace('j', 'j')  # Ensure 'j' is used for complex numbers
        result = eval(expression, {"__builtins__": None}, {"cos": cos, "sin": sin, "tan": tan, "exp": exp, "log": log, "sqrt": sqrt, "complex": complex, "rect_to_phasor": rect_to_phasor, "phasor_to_rect": phasor_to_rect})
        return result
    except Exception as e:
        return f"Error: {e}"
    

def phasor_to_rect(magnitude, angle_degrees):
    angle_radians = cmath.pi * angle_degrees / 180
    rect = cmath.rect(magnitude, angle_radians)
    # Round the real and imaginary parts to avoid small floating-point errors
    return complex(round(rect.real, 10), round(rect.imag, 10))


def rect_to_phasor(complex_number):
    magnitude = abs(complex_number)
    angle_degrees = cmath.phase(complex_number) * 180 / cmath.pi
    return magnitude, angle_degrees


if __name__ == "__main__":
    print("Complex Number Math Script")
    print("Enter a mathematical expression with complex numbers (e.g., (1 + 1j) - 1j):")
    while True:
        user_input = input(">>> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting...")
            break
        print(f"Result: {complex_math(user_input)}")