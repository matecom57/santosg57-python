import turtle

ss = 'F−G−G'
r1 = 'F−G+F+G−F'
r2 = 'GG'
teta = 120
del1 = 20

niter = 3


for i in range(niter):
  for s in ss:
    if


 for s in ss:
  if s == 'F' or s == 'G':
    turtle.forward(del1)
  elif s == '+':
    turtle.left(teta)
  else:
    turtle.right(teta)

turtle.mainloop()



