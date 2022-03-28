#las importaciones siempre deben ir en la parte superior del script

# orden de las importaciones
# 1. biblioteca estándar
# 2. biblioteca de terceros
# 3. biblioteca local del usuario

# se recomiendan las importaciones absolutas, aunque las relativas son aceptables también
# absolutas
# from modules.my_module import function_one
# from .modules.my_module import function_one

# evitar importaciones comodín 
# from modules.my_module import *

# las importaciones se deben hacer una en cada línea
import os
import sys

# si son varias importaciones del mismo módulo, se pueden poner en la misma línea
from modules.my_module import function_one, function_two

# los dunders (variables con dos __) deben ir después de las importaciones
__author__ = 'Miguel'

# varios imports, ojo con la , antes del \... NUNCA USE import *
from modules.my_module import function_one
from modules.my_module import function_two

# también es viable usar esta convención
from modules.my_module import function_one, \
    function_two