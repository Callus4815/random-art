import random
from math import *
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

functions = {
     "no idea":lambda x,y:(cos(x*80)),
     "mul": lambda x, y:sin(cos(50*y)),
     "maxi": lambda x, y:exp(cos(45*x)),
     "minni": lambda x, y:sin(pow(10)*x),
    "one_more": lambda x, y: sin(40 * sin(x * y)),
     'another': lambda x, y: exp(cos(65)+(cos(x))),
    'loco': lambda x, y: cos(cos(10 * y))}


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    choice = random.choice(list(functions.keys()))

    return Expression(choice)


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.run(x, y)

class Expression:
    def __init__(self,operator):
        self.operator = operator

    def __str__(self):
        return str(self.operator)


    def run(self, x, y):
        return functions[self.operator](x, y)
