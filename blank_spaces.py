from modules.my_module import some_function

ham = [1, 2]
eggs = 'key'

# espacios en blanco después de ",", ":" o ";"
some_function(ham[1], {eggs: 2}, 'value')

# variables solo deben tener un espacio entre el nombre y la definición
x = 3
long_variable = 'value'
b = x + 1
x += 1
y = (x+b) * (x-b)
y = x*2 + 1

# anotaciones de funciones
def saludate(name: str) -> None:
    print(f'hola, {name}')
saludate('Miguel')

# argumentos de las funciones van sin espacios entre la asignación "=", espacio entre argumentos
saludate(name='Miguel')
some_function(var_one=2, var_two=3, var_three=5)

# no poner varias claúsulas en la misma línea
# if x == 3: saludate(name='Miguel') (MAL)
# si hay else puede usar un operador ternario -> condition_if_true if condition else condition_if_false
# como por ejemplo: estado = "Es bonito" if es_bonito else "No es bonito"
if x == 3:
    saludate(name='Miguel')

    