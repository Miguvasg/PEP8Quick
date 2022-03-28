from modules.my_module import some_function

var_one_to_send_to_function = 'value 1'
var_two_to_send_to_function = 'value 2'
var_three_to_send_to_function = 'value 3'

# los argumentos deben ir alineadas con el delimitador del primer argumento
foo = some_function(var_one_to_send_to_function,
                    var_two_to_send_to_function,
                    var_three_to_send_to_function)

# agregar 4 espacios (o un nivel más de indentación) después del inicio del nombre de la función para que se
# distingan los argumentos de la función, se pueden colocar varias variables en una línea
foo = some_function(
        var_one_to_send_to_function, var_two_to_send_to_function,
        var_three_to_send_to_function)

# en las condiciones if que sobrepasen la línea pep 8 no toma una posición explícita, pero recomienda
# alinear los argumentos con el primero aunque visualmente no sea fácil de distinguir
if (var_one_to_send_to_function == 1 and
    var_two_to_send_to_function == 2):
    print('continuar con el código')

#en las listas funciona igual, se agrega un nivel de indentación
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]