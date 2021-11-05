## imports/installs: pyaudio (pipwin) -> pip install pipwin (make sure to have your path set)
## numpy (pip)




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
    if "clothes" in eq:
        eq = eq.replace("clothes", ")")
    if " million" in eq:
        eq = eq.replace(" million", "000000")
        print(eq)
    if "√" in eq:
        # print(eq)
        eq = re.sub(r"√\s?\((.+)\)", r"np.sqrt(\1)", eq)
        eq = re.sub(r"√\s?(\d+)", r"np.sqrt(\1)", eq)
        # print(eq)
    if "x" in eq:
        eq = eq.replace("x", "*")
    if "^" in eq:
        eq = eq.replace("^", "**")
    if "to the power" in eq:
        eq = re.sub(r"to the power( of)?", r"**", eq)
    if "log" in eq:
        # print(eq)
        eq = re.sub(r"log\s?\((.+)\)", r"np.log(\1)", eq)
        eq = re.sub(r"log\s?(\d+)", r"np.log(\1)", eq)
    if "e" in eq:
        eq = eq.replace("e", "np.e")
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
