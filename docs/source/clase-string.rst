Clase String
============

.. code:: Bash

   >>> x = '''
   ...  hola
   ...  como estas,
   ...  yo estoy bien'''
   >>> 
   >>> x
   '\n hola\n como estas,\n yo estoy bien'
   >>> 
   >>> len(x)
   34
   >>> type(x)
   <class 'str'>
   >>> 


   >>> y1 = "1234"
   >>> y2 = '1234'
   >>> y1 == y2

Algunos métodos de la clase string:

``'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'``

.. code:: Python

   pp = '''ya no se encantarán mis ojos en tus ojos,
   ya no se endulzará junto a ti mi dolor.

   Pero hacia donde vaya llevaré tu mirada
   y hacia donde camines llevarás mi dolor.

   Fui tuyo, fuiste mía. ¿Qué más? Juntos hicimos
   un recodo en la ruta donde el amor pasó.

   Fui tuyo, fuiste mía. Tu serás del que te ame,
   del que corte en tu huerto lo que he sembrado yo.

   Yo me voy. Estoy triste: pero siempre estoy triste.
   Vengo desde tus brazos. No sé hacia dónde voy.

   ...Desde tu corazón me dice adiós un niño.
   Y yo le digo adiós.'''


.. code:: Python
 
   len(pp)

   pp.capitalize()

   pp.count('m')

   pp.count('mi')

   pp.count('corazón')

   pp.count('\n')

   pp.count('x')

.. code:: Python

   pp.find('x')

   pp.find('ojos')

   pp.find('ojos', 25)

   pp.find('ojos', 37)

   pp.islower()

   pp.lower()

   pp.replace('\n', ' ')

   yy = pp.replace('Ya no se', 'Para tí mi Dulcinea: \n\n Ya no se')
   print(yy)

   ww = pp.split('\n')

   ww

   len(ww)

   type(ww)



 

