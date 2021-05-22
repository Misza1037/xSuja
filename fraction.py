def decompose(n):
  k = n
  r = []
  while k != 1:
    i = 2
    while k%i!=0:
      i+=1
    r.append(i)
    

class Fraction:
  def __init__(self, l):
    if type(l) != list: raise TypeError('')
    if len(l) != 2: raise ValueError('')
    self.l = l
