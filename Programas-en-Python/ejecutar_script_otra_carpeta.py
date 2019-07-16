"""
Para importar un file que esta en otra carpeta necesitamos:
- file.py
- __init__.py (Este es un archivo vacio solo con ese nombre y sirve para poder llamar a file.py)

Con sys.path.append lo que hacemos es agregar la ubicacion donde vamos a buscar el file.py sin cambiar de directorio

En este ejemplo, buscamos el nombre de usuario (os.environ['USERPROFILE']) y luego la carpeta de Desktop.
En el ultimo paso importamos file y ya queda listo.

!!!! Si quiero importar un file dentro de una carpeta llamada "passwords" que contiene un file llamado "passwd_ig.py" lo que hacemos
es agregar el __init__.py en la misma ubicacion de la carpeta y dentro de la carpeta el passwd_ig.py. La forma de importarlo:
from passwords import passwd_ig
"""


import os, sys
sys.path.append(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

import file
from passwords import passwd_ig
