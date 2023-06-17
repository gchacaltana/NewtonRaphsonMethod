"""
Aplicación para aplicar el algoritmo numérico de Newton Raphson
en ecuaciones no lineales.
"""
__author__ = "Gonzalo Chacaltana Buleje"

import os
import logging
import sympy as sy
from newton_raphson import NewtonRaphson
# from sympy.parsing.latex import parse_latex


class Application(object):
    """
    Clase que implementa la aplicación principal
    """

    def __init__(self, x, max_error):
        self.initial_x = x
        self.max_error = max_error
        self.x = sy.Symbol('x')
        self.config = {}
        self.config['initial_temp'] = self.initial_x
        self.config['rounding'] = 3
        self.config['max_error'] = self.max_error

    def f(self, x):
        """
        Función f(x) que contiene la ecuación que proporciona la temperatura
        a la que se debe enfriar el muñón para obtener la contracción deseada.
        """
        return -0.50598*10**-10*x**3 + 0.38292 * \
            10**-7*x**2 + 0.74363*10**-4*x + 0.88318*10**-2

    def run(self):
        """
        Método principal de la aplicación.
        """
        nr = NewtonRaphson(self.x, self.f(self.x), self.config)
        nr.run()


if __name__ == "__main__":
    try:
        os.system('clear')
        print("\n Aplicacion del Metodo de Newton-Raphson para resolver ecuaciones no lineales")
        print(
            "-----------------------------------------------------------------------------")
        x: float = float(
            input("\n Ingrese el valor inicial de la temperatura de la mezcla: "))
        max_error: float = float(
            input("\n Ingrese el valor maximo del error absoluto relativo (%): "))
        app = Application(x, max_error)
        app.run()
    except (Exception, TypeError, IndexError) as err:
        logging.error(str(err))
