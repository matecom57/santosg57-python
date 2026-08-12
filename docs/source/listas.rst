Listas
======

Una lista es una estructura de datos definida por corchetes [ ].

**Ejemplos**

.. code:: Python

   x = [1,2,33,5,6,7,8]
   
   y = []

   z = ['Juan', 'Pedro', 'Maria']

   w = [x, z]   # w es la variable construida a partir de las variables x & y

   k = ['Juan', [20, 80]]

**Algunos métodos:**

``append``, ``clear``, ``copy``, ``count``, ``index``, ``insert``, ``pop``, ``remove``, ``sort``

**Ejemplos**

.. code:: Python

   nombre = 'Juan'
   peso = 80
   edad = 60

   sujeto = [nombre, peso, edad]

   sujeto.append('Maria')

   sujeto2 = sujeto.copy()

   sujeto.count()

   i = sujeto.index('80')

   sujeto
