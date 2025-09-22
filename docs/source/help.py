y = {'pesos':[45, 64, 70], 'edad': 65, 'nombres': ('Juan', 'Pedro')}

print(type(y))

print(len(y))

dd = dir(y)

for ss in dd:
  if not ss[0] == '_':
    print(help(y.ss))




