# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"

import sympy as sy

class NewtonRaphson(object):

    def __init__(self, x, fx, options):
        self.x, self.fx = x, fx
        self.options = options
        self.limit_error = 1
        self.iterations, self.max_iterations = 0, 20

    def set_options(self):
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self._x = self.options['initial_root'] if self.options['initial_root'] else 0

    def run(self):
        self.set_options()
        while(self.iterations < self.max_iterations):
            self.iterations = self.iterations+1
            self.calculate_root()
            self.calculate_error()
            self.evaluate()

    def calculate_root(self):
        print("Iteracion {}".format(self.iterations))
        print("Estimacion de la raiz, cuando x = {}".format(self._x))
        self._y = round(self._x-(self.fx.subs(self.x, self._x) /
                                 self.df().subs(self.x, self._x)), self.rounding)
        print("Obtenemos: y = {}".format(self._y))

    def calculate_error(self):
        self.error = (abs((self._y - self._x)/self._y))*100
        print("Aproximacion del error absoluto: {}".format(str(self.error)+" %"))

    def evaluate(self):
        stop = True if self.error<self.limit_error else False
        if stop : raise Exception("Stop")
        self._x = self._y

    def df(self):
        return sy.diff(self.fx, self.x)
