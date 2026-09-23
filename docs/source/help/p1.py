import math

s = dict()

dic = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

for ss in dic:
  print('%%%%%%%%%%%%%%%%%%%%%%%%%%%% '+ss)
  print(help(eval('s.'+ss)))




