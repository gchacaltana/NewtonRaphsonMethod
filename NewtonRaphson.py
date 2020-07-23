# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"

import numpy as np
import sympy as sy

class NewtonRaphson(object):
    def __init__(self, x, fx):
        self.x, self.fx = x, fx

    def root(self,_x, decimal_points):
        return round(_x-(self.fx.subs(x,_x)/self.df().subs(x,_x)),decimal_points)

    def df(self):
        return sy.diff(self.fx,self.x)

if __name__ == "__main__":    
    def f(x):return -0.50598*10**-10*x**3 + 0.38292*10**-7*x**2 + 0.74363*10**-4*x + 0.88318*10**-2
    x = sy.Symbol('x')
    fx = f(x)
    nr = NewtonRaphson(x,fx)    
    #sy.pprint(nr.df().subs(x,5))