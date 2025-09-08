Ejemplos_sep2825
====================

1)

.. code:: Python

   import turtle

   screen = turtle.Screen()

   screen.setup(width=800, height=600)

   t = turtle.Turtle()
   t.forward(100)

   turtle.done()

2)

Dados lss siguientes series de puntos, encontrar la mejor recta :mat:`y= \beta_0 + \beta_1 x`. Donde:

.. math:

   \beta_1 = \frac{\sum_{i=1}^n x_iy_i - n \bar{x}\bar{y}}{\sum_{i=1}^n x_i^2 - \frac{1}{n} (\sum_{i=1}^n x_i)^2}

   \beta_0 = \bar{y} - \beta_1 \bar{x}


[1]  1.00  2.00  3.00  4.00  5.00  6.00  7.00  8.00  9.00 10.00 11.00 12.00
[13]  1.23  2.13  1.42 -0.69  4.29  3.64  9.30 10.62  7.42  8.40 12.30 10.30

