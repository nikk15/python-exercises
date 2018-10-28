import math

def pi(n):
    return "PI with {} cases is:  {:.{}f}".format(n, math.pi, n)

def decimal():
    dec = " "
    while dec == " " or dec > 50:
        try:
            print("Please enter the number of decimal places, 50 or less, to round PI:")
            dec = int(input())
        except ValueError:
            print("Oops, that's not a number - try again.")
            continue
    return dec

pi(decimal())