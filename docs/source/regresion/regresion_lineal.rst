Regresión Lineal
================

En estadística, la regresión lineal o ajuste lineal es un modelo matemático usado para 
aproximar la relación de dependencia entre una variable dependiente 
:math:`Y, m` variables independientes :math:`X_i` con :math:`m \in \mathbb{Z}^{+}` y un 
término aleatorio :math:`\varepsilon`. 

**Regresión lineal simple**

El modelo de regresión lineal simple sólo está conformado por dos variables estadísticas 
llamadas :math:`X` y :math:`Y`. Considera una única variable independiente o explicativa, 
`:math:`X`, y una variable dependiente o respuesta, :math:`Y`, asumiendo que la relación entre ambas es lineal. 

.. math::

   Y = \beta_0 + \beta_1 X + \varepsilon 

donde :math:`\beta_0, \beta_1 \in \mathbb{R}'  son constantes desconocidas llamadas 
coeficientes de regresión.

**Calculo de los coeficientes de regresión**

.. math::

   {\displaystyle {\begin{aligned}{\hat {\beta }}_{1}&={\frac {\displaystyle \sum_{i=1}^{n}x_{i}y_{i}-n{\bar {x}}{\bar {y}}}{\displaystyle \sum_{i=1}^{n}x_{i}^{2}-{\frac{1}{n}}\left(\sum _{i=1}^{n}x_{i}\right)^{2}}}\\{\hat {\beta }}_{0}&={\frac {\displaystyle \sum_{i=1}^{n}x_{i}^{2}\sum _{i=1}^{n}y_{i}-\sum _{i=1}^{n}x_{i}y_{i}\sum_{i=1}^{n}x_{i}}{\displaystyle n\sum _{i=1}^{n}x_{i}^{2}-\left(\sum_{i=1}^{n}x_{i}\right)^{2}}}={\bar {y}}-{\hat {\beta }}_{1}{\bar {x}}\end{aligned}}}

**Ejemplo**

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = [1,2,3,4,5,6]
   Y = [7000, 9000, 5000, 11000, 10000, 13000]

   model = np.polyfit(x, Y, 1)

   predict = np.poly1d(model)

   print(predict)

   print("7 = {}".format(predict(7)))

   xx = [1, 7]
   yy = predict(xx)
   print(yy)

   plt.plot(x,Y, 'o')
   plt.plot(xx,yy, linewidth=3)

   plt.show(

