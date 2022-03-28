# Limite todas las líneas

Limite todas las líneas a un máximo de 79 caracteres.
Para bloques de texto largos y fluidos con menos restricciones estructurales (docstrings o comentarios),
la longitud de la línea debe limitarse a 72 caracteres.

Limitar el ancho requerido de la ventana del editor permite tener varios archivos abiertos uno al lado
del otro y funciona bien cuando se usan herramientas de revisión de código que presentan las dos versiones
en columnas adyacentes.

El ajuste predeterminado en la mayoría de las herramientas interrumpe la estructura visual del código,
lo que lo hace más difícil de entender. Los límites se eligen para evitar el ajuste en editores con el 
ancho de ventana establecido en 80, incluso si la herramienta coloca un glifo de marcador en la columna 
final al ajustar líneas. Algunas herramientas basadas en la web pueden no ofrecer ajuste de línea dinámico 
en absoluto.

Algunos equipos prefieren fuertemente una longitud de línea más larga. Para el código mantenido exclusiva 
o principalmente por un equipo que puede llegar a un acuerdo sobre este tema, está bien aumentar el límite 
de longitud de la línea hasta 99 caracteres, siempre que los comentarios y las cadenas de documentación 
sigan envueltos en 72 caracteres.

La biblioteca estándar de Python es conservadora y requiere limitar las líneas a 79 caracteres (y las 
cadenas de documentación/comentarios a 72).

La forma preferida de envolver líneas largas es usando la continuación de línea implícita de Python 
dentro de paréntesis, corchetes y llaves. Las líneas largas se pueden dividir en varias líneas colocando 
expresiones entre paréntesis. Estos deben usarse en lugar de usar una barra invertida para la continuación 
de la línea.

Las barras invertidas aún pueden ser apropiadas a veces. Por ejemplo, las declaraciones largas y 
múltiples withno podían usar la continuación implícita antes de Python 3.10, por lo que las barras 
invertidas eran aceptables para ese caso:

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
    
# Comentarios

Los comentarios que contradicen el código son peores que no comentar. ¡Tenga siempre como prioridad mantener los comentarios actualizados cuando cambie el código!

Los comentarios deben ser oraciones completas. La primera palabra debe estar en mayúscula, a menos que sea un identificador que comience con una letra minúscula (¡nunca altere el caso de los identificadores!).

Los comentarios en bloque generalmente consisten en uno o más párrafos construidos a partir de oraciones completas, y cada oración termina en un punto.

Debe usar dos espacios después de un punto final de oración en comentarios de varias oraciones, excepto después de la oración final.

Asegúrese de que sus comentarios sean claros y fácilmente comprensibles para otros hablantes del idioma en el que está escribiendo.

Codificadores de Python de países de habla no inglesa: escriba sus comentarios en inglés, a menos que esté 120 % seguro de que el código nunca será leído por personas que no hablen su idioma.

# Comentarios en línea

Utilice los comentarios en línea con moderación.

Un comentario en línea es un comentario en la misma línea que una declaración. Los comentarios en línea deben estar separados por al menos dos espacios de la declaración. Deben comenzar con un # y un solo espacio.

Los comentarios en línea son innecesarios y, de hecho, distraen si dicen lo obvio. No hagas esto:

x = x + 1                 # Increment x

Pero a veces, esto es útil:

x = x + 1                 # Compensate for border

# Cadenas de documentación

Las convenciones para escribir buenas cadenas de documentación (también conocidas como "docstrings") están inmortalizadas en PEP 257 .

Escriba cadenas de documentación para todos los módulos, funciones, clases y métodos públicos. Las cadenas de documentos no son necesarias para los métodos no públicos, pero debe tener un comentario que describa lo que hace el método. Este comentario debe aparecer después de la deflínea.
PEP 257 describe buenas convenciones de cadenas de documentación. Tenga en cuenta que lo más importante es """que el final de una cadena de documentación multilínea debe estar en una línea por sí mismo:
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
Para docstrings de una sola línea, mantenga el cierre """en la misma línea:
"""Return an ex-parrot."""