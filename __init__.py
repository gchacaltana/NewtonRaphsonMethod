# -*- coding: utf-8 -*-
from NewtonRaphson import NewtonRaphson
import sympy as sy

if __name__ == "__main__":
    try:
        def f(x): return -0.50598*10**-10*x**3 + 0.38292 * \
            10**-7*x**2 + 0.74363*10**-4*x + 0.88318*10**-2
        x = sy.Symbol('x')
        options = {
            "initial_root":-100,
            "rounding": 2
        }
        nr = NewtonRaphson(x, f(x), options)
        nr.run()
    except (Exception, TypeError,IndexError) as err:
        print("Exception: ", err)
    # sy.pprint(nr.df().subs(x,5))
