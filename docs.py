# las funciones de una sola línea deben cerrarse en la misma línea
# la primera letra debe ir en mayúscula

class Animal:
    """Clase que describe un animal (breve descripción, como un titulo)

    Un animal se describe a través de sus acciones, lo que come y bla bla bla (detalle)
    
    Atributos:
        value1: primer valor
        value2: segundo valor

    Excepciones:
        TypeError: si el valor está errado
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saltar(self):
        """Función para hacer saltar al animal

        Esta función hace que el animal salte y bla bla bla
        
        Returns:
            None
        """