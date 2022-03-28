# comparaciones con None deben hacerse con "is"
my_var = None
if my_var is None:
    print('es None')

# utilice el operador en su lugar correcto 
# NO! -> if not foo is None:
if my_var is not None:
    print('no es None')

# las excepciones deben heredar de Exception
class MyException(Exception):
    pass

# limite las claúsulas dentro de los try a las mínimas posible, use else de ser posible
try:
    value = my_var
except KeyError:
    error = True
else:
    error = False

# Cuando un recurso es local para una sección particular de código, use una 
# declaración "with" para asegurarse de que se limpie de manera rápida y confiable después
#  de su uso, OJO con with siguen saliendo excepciones!
def read_data_from_file():
    with open("welcome.txt") as file:
        data = file.read()
    return data

# no usar prefijos para cortar cadenas
# NO usar if foo[:3] == 'bar':
foo = 'barcito'
if foo.startswith('bar'):
    print('inicia con bar')

# las comparaciones de clases se hacen con isinstance
if isinstance(foo, str):
    print('es una cadena')

# para listas, cadenas tuplas, las secuencias vacías son falsas
my_list = []
if my_list:
    print('no es vacía')

# NO compare booleanos con == True o == False
if error:
    print('es True')
