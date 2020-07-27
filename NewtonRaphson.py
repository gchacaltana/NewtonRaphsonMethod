# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"

import sympy as sy
import sys
import os
from matplotlib import pyplot as plt


class NewtonRaphson(object):

    def __init__(self, x, fx, options):
        self.x, self.fx = x, fx
        self.coord_x, self.coord_y = [], []
        self.options = options
        self.iterations, self.max_iterations = 0, 20

    def set_options(self):
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self._x = self.options['initial_temp'] if self.options['initial_temp'] else 0
        self.max_error = self.options['max_error'] if self.options['max_error'] else 0.5
        self.initial_x = self._x

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
            self.calculate()
            self.calculate_error()
            self.evaluate()

    def calculate(self):
        print("\nIteracion {}".format(self.iterations))
        print("---------------")
        print("Cuando x = {}".format(self._x))
        self._y = self.estimate_root(self._x)
        print("Obtenemos: f(x) = f({}) = {}".format(self._x, self._y))
        self.coord_x.append(self._x)
        self.coord_y.append(self._y)

    def estimate_root(self, x):
        return round(x-(self.fx.subs(self.x, x) / self.df().subs(self.x, x)), self.rounding)

    def calculate_error(self):
        self.error = round((abs((self._y - self._x)/self._y))
                           * 100, self.rounding)
        print("Error absoluto relativo: {}".format(str(self.error)+" %"))

    def evaluate(self):
        if (self.error < self.max_error):
            print("El error absoluto relativo {} % es menor que el valor maximo esperado {} %".format(
                self.error, self.max_error))
            self.print_result()
            self.show_graph()
            sys.exit()
        else:
            print("El error absoluto relativo {} % es mayor que el valor maximo esperado {} %".format(
                self.error, self.max_error))
            self._x = self._y

    def df(self):
        return sy.diff(self.fx, self.x)

    def print_result(self):
        print("\n------------------------------------------")
        print("Resultado Metodo Newton-Raphson:")
        print("------------------------------------------")
        print("\nLa temperatura que se necesita para enfriar el munon es: {}*F".format(self._x))
        print("\nValores obtenidos")
        for k in range(len(self.coord_x)):
            print("iteracion {}: f(x)=> ({},{}) ".format(
                k+1, self.coord_x[k], self.coord_y[k]))

    def show_graph(self):
        input("\n[Enter] para mostrar grafico")
        self.coord_x, self.coord_y = [], []
        for i in range(int(self.initial_x), int(self._x),-1):
            self.coord_x.append(i)
            self.coord_y.append(self.estimate_root(i))
        self.coord_x.append(self._x)
        self.coord_y.append(self.estimate_root(self._x))

        plt.style.use('classic')
        plt.scatter(self.coord_x, self.coord_y,
                    alpha=0.5, color="royalblue", s=75)
        plt.grid(True)
        plt.ylabel("f(x)")
        plt.xlabel("x = Temperatura de mezcla (en F°)")
        plt.title("Gráfico: Resultado de f(x) aplicando Metodo de Newton-Raphson")
        plt.show()
