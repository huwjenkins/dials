from __future__ import division
import sympy

symbols = 'x y'
functions = 'sin cos pi'
f = '(x*x + y*y + pi * sin(x) + pi * cos(y)) ** 2'

x, y = sympy.symbols(symbols)
dfdx = sympy.diff(f, x)
dfdy = sympy.diff(f, y)
dfdxx = sympy.diff(dfdx, x)
dfdxy = sympy.diff(dfdx, y)
dfdyx = sympy.diff(dfdy, x)
dfdyy = sympy.diff(dfdy, y)

fout = open('fJH.py', 'w')
fout.write('def f(%s):\n' % ''.join(symbols.split()))
fout.write('    import numpy\n')
fout.write('    from math import %s\n' % ', '.join(functions.split()))
fout.write('    %s = %s\n' % (', '.join(symbols.split()),
                              ''.join(symbols.split())))
fout.write('    return %s\n' % f)
fout.write('def J(%s):\n' % ''.join(symbols.split()))
fout.write('    import numpy\n')
fout.write('    from math import %s\n' % ', '.join(functions.split()))
fout.write('    %s = %s\n' % (', '.join(symbols.split()),
                              ''.join(symbols.split())))
fout.write('    return numpy.array([%s, %s])\n' % (dfdx, dfdy))
fout.write('def H(%s):\n' % ''.join(symbols.split()))
fout.write('    import numpy\n')
fout.write('    from math import %s\n' % ', '.join(functions.split()))
fout.write('    %s = %s\n' % (', '.join(symbols.split()),
                              ''.join(symbols.split())))
fout.write('    return numpy.matrix([[%s, %s], [%s, %s]])\n' % \
    (dfdxx, dfdxy, dfdyx, dfdyy))

