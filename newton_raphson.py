"""
NewtonRapshon.py
El método Newton-Raphson, es un algoritmo numérico utilizado para encontrar 
las raíces de una función.
"""
__author__ = "Gonzalo Chacaltana"

import sys
import os
import sympy as sy
from matplotlib import pyplot as plt


class NewtonRaphson(object):
    """
    Clase para implementar el algoritmo numperico Newton Raphson 
    """
    def __init__(self, x, fx, options):
        self.x, self.fx = x, fx
        self.coord_x, self.coord_y = [], []
        self.options = options
        self.iterations, self.max_iterations = 0, 20
        self.error = 0

    def set_options(self):
        """
        Método para asignar valores
        """
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self._x = self.options['initial_temp'] if self.options['initial_temp'] else 0
        self.max_error = self.options['max_error'] if self.options['max_error'] else 0.5
        self.initial_x = self._x

    def run(self):
        """
        Método principal de la clase.
        """
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
        """
        Método para calcular la función
        """
        print(f"\nIteracion {self.iterations}")
        print("-"*30)
        print(f"Cuando x = {self._x}")
        self._y = self.estimate_root(self._x)
        print(f"Obtenemos: f(x) = f({self._x}) = {self._y}")
        self.coord_x.append(self._x)
        self.coord_y.append(self._y)

    def estimate_root(self, x):
        """
        Método para estimar la raíz
        """
        return round(x-(self.fx.subs(self.x, x) / self.df().subs(self.x, x)), self.rounding)

    def calculate_error(self):
        """
        Método para calcular el error
        """
        self.error = round((abs((self._y - self._x)/self._y))
                           * 100, self.rounding)
        print(f"Error absoluto relativo: {self.error} %")

    def evaluate(self):
        """
        Método para evaluar el error relativo
        """
        if (self.error < self.max_error):
            print(f"El error absoluto relativo {self.error} % es menor que el valor maximo esperado {self.max_error} %")
            self.print_result()
            self.show_graph()
            sys.exit()
        else:
            print(f"El error absoluto relativo {self.error} % es mayor que el valor maximo esperado {self.max_error} %")
            self._x = self._y

    def df(self):
        """
        Método para encontrar la diferenciación de la expresión matemática
        """
        return sy.diff(self.fx, self.x)

    def print_result(self):
        """
        Método que muestra resultado
        """
        print("\n")
        print("-"*45)
        print("Resultado Metodo Newton-Raphson:")
        print("-"*45)
        print(f"\nLa temperatura que se necesita para enfriar el munon es: {self._x}*F")
        print("\nValores obtenidos")
        for k in range(len(self.coord_x)):
            print("iteracion {}: f(x)=> ({},{}) ".format(
                k+1, self.coord_x[k], self.coord_y[k]))

    def show_graph(self):
        """
        Método que muestra gráfico de la función
        """
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
