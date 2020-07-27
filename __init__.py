# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
from NewtonRaphson import NewtonRaphson
import sympy as sy
from sympy.parsing.latex import parse_latex
import os

class Application(object):
    def __init__(self):
        self.x, self.config = sy.Symbol('x'), {}

    def f(self,x):
        """
        Función f(x) que contiene la ecuación que proporciona la temperatura
        a la que se debe enfriar el muñón para obtener la contracción deseada.
        """
        return -0.50598*10**-10*x**3 + 0.38292 * \
            10**-7*x**2 + 0.74363*10**-4*x + 0.88318*10**-2

    def run(self):
        self.input_values()
        self.setConfig()
        self.run_newton_raphson()

    def input_values(self):
        os.system('clear')
        print("\n")
        print("Aplicacion del Metodo de Newton-Raphson para resolver ecuaciones no lineales")
        print("-----------------------------------------------------------------------------")
        self.initial_x = float(
            input("\nIngrese el valor inicial de la temperatura de la mezcla: "))
        self.max_error = float(
            input("Ingrese el valor maximo del error absoluto relativo (%): "))

    def setConfig(self):
        self.config['initial_temp'] = self.initial_x
        self.config['rounding'] = 3
        self.config['max_error'] = self.max_error

    def run_newton_raphson(self):
        nr = NewtonRaphson(self.x, self.f(self.x), self.config)
        nr.run()


if __name__ == "__main__":
    try:
        app = Application()
        app.run()
    except (Exception, TypeError, IndexError) as err:
        print("Exception: ", err)
