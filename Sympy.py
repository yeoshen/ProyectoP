# To ignore numpy errors:
#     pylint: disable=E0611,E0401,E0602

'''
Este programa permite evaluar una formula->función f(var1,var2,var3...) on the fly
'''
from sympy import *
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application)
import os

# Este comentario lo estoy insertando con la rama nuevas modificaciones

os.system('clear')

funcion = input(
    'Introduzca la función con sus variables: f(var1,var2,var3...) = ')

# Convertir la función introducida en función válida Sympy.
# Otra manera de convertir strings a funciones Sympy es con: sympify(<FUNCTION EN STRING>)
f = parse_expr(funcion, transformations=(
    standard_transformations + (implicit_multiplication_application,)))

# Extraer e identificar sus componentes.
# Ej: variables, números, signos, portencias, etc
componentes = srepr(f)

# Se extraen las variables identificadas con la función Symbol('<VARIABLE>')
variables = [(variable[variable.find("('")+2:variable.find("('")+3])
             for variable in componentes.split(',') if variable.find('Symbol') is not -1]

# Obtener variables de la formula y eliminar variables repetidas y ordenarlas
variables = sorted(list(dict.fromkeys(variables).keys()))

# FORMULAS DE EJEMPLO
# x**3+2*y+z+c+((a*b)**2+4)/x
# cos(x)+ b + x + ((a*b)**2+4)/x

# Crear diccionario para reemplazar las variables en la fórmula
v = {}
var = ""
for variable in variables:
    valor = float(input('Valor de {}: '.format(variable)))
    v[variable] = valor
    var += variable + ","

var = var[:len(var)-1]

print("f({}) = {}".format(str(var), f))
resultado = float(f.subs(v))

print(round(resultado, 2))
