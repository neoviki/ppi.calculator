'''
    Pixels Per Inch Calculator.
    This script calculates PPI value for a display given its resolution and screen size ( diagonal length )


    Author  : Viki (a) Vignesh Natarajan
    Contact : vikiworks.io
'''
import sys
import math

def calculate_ppi(d, px, py):
    ppi = (math.sqrt(((px*px) + (py*py)))) / d
    return ppi

diagonal_length=""
res_x=""
res_y=""
argc=len(sys.argv)
print("")

if argc < 4:
    #print("usage: ppi_calculator.py <screen diagonal length in inches> < screen resolution x > < screen resolution y >")
    print("\n\nFEED YOUR DISPLAY DETAILS:\n")
    inp = input("\tEnter the screen size ( in inches ) \t: ")
    diagonal_length=float(inp)
    inp = input("\tEnter the screen resolution ( x-axis ) \t: ")
    px=int(inp)
    inp = input("\tEnter the screen resolution ( y-axis ) \t: ")
    py=int(inp)
else:
    diagonal_length=float(sys.argv[1])
    px=int(sys.argv[2])
    py=int(sys.argv[3])

print("\n\nINPUTS:\n\n")

print("\tDiagonal Length ( Inches ) \t\t: ", diagonal_length)
print("\tResolution ( x ) \t\t\t: ", px)
print("\tResolution ( y ) \t\t\t: ", py)

ppi=calculate_ppi(diagonal_length, px, py)
print("\n\nRESULT:\n\n")
print("\tPPI ( Pixels per Inch ) \t\t: ", ppi)
print("")

