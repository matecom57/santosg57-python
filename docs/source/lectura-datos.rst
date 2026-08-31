Lectura de texto de archivos
============================

Ejemplo para lee un archivo de texto:

**Ejemplo 1.**

.. Python

   fil = open('dir.txt', 'r')
  
   datos = fil.read()

   type(datos)

**Ejemplo 2.**

   fil = open('dir.txt', 'r')

   datos = fil.readlines()

   type(datos)
