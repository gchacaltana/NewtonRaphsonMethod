# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"

import sympy as sy
import sys,os


class NewtonRaphson(object):

    def __init__(self, x, fx, options):
        self.x, self.fx = x, fx
        self.options = options
        self.iterations, self.max_iterations = 0, 20

    def set_options(self):
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self._x = self.options['initial_root'] if self.options['initial_root'] else 0
        self.max_error = self.options['max_error'] if self.options['max_error'] else 0.5

    def run(self):
        self.set_options()
        os.system('clear')
        print("\nDada la funcion f(x)")
        print("\nf(x) = {}".format(self.fx))
        while(self.iterations < self.max_iterations):
            self.iterations = self.iterations+1
            self.calculate_root()
            self.calculate_error()
            self.evaluate()

    def calculate_root(self):
        print("\nIteracion {}".format(self.iterations))
        print("-------------------")
        print("Estimacion de la raiz, cuando x = {}".format(self._x))
        self._y = round(self._x-(self.fx.subs(self.x, self._x) /
                                 self.df().subs(self.x, self._x)), self.rounding)
        print("Obtenemos: y = {}".format(self._y))

    def calculate_error(self):
        self.error = (abs((self._y - self._x)/self._y))*100
        print("Error absoluto: {}".format(str(self.error)+" %"))

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
