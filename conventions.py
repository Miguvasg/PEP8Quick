# nombres de paquetes y módulos -> cortos y en minúscula ejemplo: django.py

# Clases
class CapWords:
    pass

# Excepciones -> CamelCase con sufijo Error
class CustomError(Exception):
    pass

# funciones y variables -> lower_case_with_underscores
my_custom_variable = True
def my_custom_function():
    pass
# las constantes se definen con mayúsculas
CONSTANTE = 3.14

# métodos y variables de instancia, deben estar con doble guión bajo, estos no pueden ser
# accedidos desde afuera, en este caso la variable __name o la función __get_name no pueden
# accederse desde afuera de la instancia
class MyClass:

    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def get_name(self):
        return self.__get_name()
