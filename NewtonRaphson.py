# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"

import sympy as sy
import sys
import os


class NewtonRaphson(object):

    def __init__(self, x, fx, options):
        self.x, self.fx = x, fx
        self.options = options
        self.iterations, self.max_iterations = 0, 20

    def set_options(self):
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self._x = self.options['initial_temp'] if self.options['initial_temp'] else 0
        self.max_error = self.options['max_error'] if self.options['max_error'] else 0.5

    def run(self):
        self.set_options()
        os.system('clear')
        print("\nDada la funcion f(x)")
        print("\nf(x) = {}".format(sy.simplify(self.fx)))
        print("\nDonde: x = T = Temperatura de la mezcla")
        print("\n------------------------------------------")
        print("Aplicando el Metodo de Newton-Raphson")
        print("------------------------------------------")
        while(self.iterations < self.max_iterations):
            self.iterations = self.iterations+1
            self.calculate_root()
            self.calculate_error()
            self.evaluate()

    def calculate_root(self):
        print("\nIteracion {}".format(self.iterations))
        print("---------------")
        print("Cuando x = {}".format(self._x))
        self._y = round(self._x-(self.fx.subs(self.x, self._x) /
                                 self.df().subs(self.x, self._x)), self.rounding)
        print("Obtenemos: f(x) = f({}) = {}".format(self._x,self._y))

    def calculate_error(self):
        self.error = round((abs((self._y - self._x)/self._y))*100,self.rounding)
        print("Error absoluto relativo: {}".format(str(self.error)+" %"))

    def evaluate(self):
        if (self.error < self.max_error):
            print("El error absoluto relativo {} % es menor que el valor maximo esperado {} %".format(
                self.error, self.max_error))
            sys.exit()
        else:
            print("El error absoluto relativo {} % es mayor que el valor maximo esperado {} %".format(
                self.error, self.max_error))
            self._x = self._y

    def df(self):
        return sy.diff(self.fx, self.x)
