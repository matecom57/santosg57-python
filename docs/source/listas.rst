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

**Operaciones en Listas**

.. code:: Python

   x = [2,1,3]
   y = [4,3,4]

   x+y

   2*x

   x^2

   len(x)

   x[1]

   x[-1]

   x = [1,2,2,3,4,2,3,5,4]

   x == 3

   x > 3

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

   sujeto.insert(1, 'Gonzalez')

   sujeto.remove('Maria')

   sujeto.pop()

   sujeto.sort()

.. code:: Python

   texto = ["B", "B", "C", "A", "A", "A", "B",
   "C", "A", "B", "A", "B", "B", "A",
   "A", "B", "A", "B", "C", "A", "A",
   "A", "C", "B", "A", "B", "A", "A",
   "B", "A", "A", "C", "A", "B", "C",
   "C", "B", "A", "C", "A", "A", "A",
   "A", "A", "A", "B", "A", "B", "A",
   "B"]

   texto.count('A')

   i = texto.index('and')

   len(texto)

   texto.sort()

   texto.index('C')
