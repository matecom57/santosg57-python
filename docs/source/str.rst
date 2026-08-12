Clase String´s
==============

Un string se define como una secuencia de caracteres.

**Ejemplos:**

.. code:: Python

   '1234567890'

   "1234567890"

**NOTA** No se puede modificar los elementos de una string.

**Operaciones en string's**

.. code:: Python

   x = 'Juan'
   y = 'Gonzalez'

   x+y 

   z= x + ' ' + y 

   2*x

   x[0]

   z[:4]

   z[4:]

   z[5:8]

**Algunos Métodos**

`count`, `find`, `isalnum`, `isalpha`, `lower`, `replace`, `rfind`, `split`, `upper`

**Ejemplo:**

.. code:: Python

   texto = '''Parkinson's disease is a progressive neurodegenerative disease characterized by tremor and bradykinesia 
   and is a common 
   neurologic ailment. Male sex and advancing age are independent risk factors and, as the population ages, is taking an 
   increasing toll on productivity and medical resources. There are a number of other extrapyramidal conditions that can 
   make the diagnosis challenging. Unlike other neurodegenerative diseases, idiopathic Parkinson's disease has effective 
   treatments that mitigate symptoms. Medications can improve day-to-day function and, in cases where medication does 
   not 
   give a sustained benefit or has significant side effects, treatments like deep brain stimulation result in improved 
   quality of life.
   '''

   len(texto)

   texto.count('and')

   textoN = texto.lower()

   textoN = textoN.replace('\n', ' ')

   tt = textoN.split(' ')


