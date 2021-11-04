## imports/installs: pyaudio




### To do: check all possibilities and see what needs tidying

import numpy as np
import re

def tidy(eq):
    eq = eq.lower()
    # print(eq)
    ## million
    # print((" million" in eq))
    if "open" in eq:
        eq = eq.replace("open", "(")
    if "close" in eq:
        eq = eq.replace("close", ")")
    if " million" in eq:
        eq = eq.replace(" million", "000000")
        print(eq)
    if "√" in eq:
        # print(eq)
        eq = re.sub(r"√\s?(\d+)", r"np.sqrt(\1)", eq)
        # print(eq)
    if "x" in eq:
        eq = eq.replace("x", "*")
    if "^" in eq:
        eq = eq.replace("^", "**")
    if "to the power" in eq:
        eq = re.sub(r"to the power( of)?", r"**", eq)
    ## Remove spaces
    eq = eq.replace(" ", "")
    return eq

def calculate(equation):
    eq = tidy(equation)
    # print(eq)
    try:
        res = eval(eq)
    except:
        res = None
    return eq, res
