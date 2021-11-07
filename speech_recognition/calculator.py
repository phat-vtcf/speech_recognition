## imports/installs: pyaudio (pipwin) -> pip install pipwin (make sure to have your path set)
##                   numpy (pip)


import numpy as np
import re

def tidy(eq):
    ## Make everything lowercase
    eq = eq.lower()
    ## Replace 'open' and 'close' by brackets
    if "open" in eq:
        eq = eq.replace("open", "(")
    if "close" in eq:
        eq = eq.replace("close", ")")
    ## In some contexts, it recognises 'close' as 'clothes'
    if "clothes" in eq:
        eq = eq.replace("clothes", ")")
    ## If you say e.g. one million, it will write it as 1 million instead of 1000000
    if " million" in eq:
        eq = eq.replace(" million", "000000")
        print(eq)
    ## It recognises 'the square root of' as '√'
    if "√" in eq:
        ## Check first if there are brackets to include everything between the brackets
        ## in the square root
        eq = re.sub(r"√\s?\((.+)\)", r"np.sqrt(\1)", eq)
        eq = re.sub(r"√\s?(\d+)", r"np.sqrt(\1)", eq)
    ## 'Times' is written as an 'x'
    if "x" in eq:
        eq = eq.replace("x", "*")
    ## 'To the power (of)' is either written in words or as a '^'
    if "^" in eq:
        eq = eq.replace("^", "**")
    if "to the power" in eq:
        eq = re.sub(r"to the power( of)?", r"**", eq)
    ## Convert log (e log) to numpy.log so that it can be evaluated
    if "log" in eq:
        ## Check for brackets first
        eq = re.sub(r"log\s?\((.+)\)", r"np.log(\1)", eq)
        eq = re.sub(r"log\s?(\d+)", r"np.log(\1)", eq)
    ## Convert e to numpy.e so that it can be evaluated
    if "e" in eq:
        eq = eq.replace("e", "np.e")
    ## Remove spaces
    eq = eq.replace(" ", "")
    return eq

def calculate(equation):
    ## Convert the equation to one that can be evaluated
    eq = tidy(equation)
    try:
        res = eval(eq)
    except:
        ## If the string cannot be evaluated, None is given back, and
        ## the user will be asked to try again
        res = None
    return eq, res
