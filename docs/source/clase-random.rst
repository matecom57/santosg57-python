Clase random
============

.. code:: Python

   import random

Algunos métodos:

``'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'``

Algunos métodos y ejemplos:

.. code:: Python

   import random

   random.gauss()

   round(random.gauss(),2)

   random.randint(1,100)

   random.random()

   ss = random.sample(['red', 'blue'], counts=[4, 2], k=5)
   print(ss)
   type(ss)

   random.uniform(1,10)


    


