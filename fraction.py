def dc(n):
  k = n
  r = []
  while k != 1:
    i = 2
    while abs(k)%i!=0 and abs(k) != 1:
      #print(i)
      #print(k)
      #print()
      i+=1
    r.append(i)
    k = k//i
  return r if r != [] else [1]


def common(a,b):
  c = [value for value in a if value in b]
  return c


class Fraction:
  def __init__(self, l):
    if type(l) != list: raise TypeError('')
    if len(l) != 2: raise ValueError('')
    self.l = l
  def __str__(self):
    self.cut()
    return str(self.l[0])+'/'+str(self.l[1])
  def __add__(self, other):
      r = [None, None]
      r[0] = self.l[0]*other.l[1] + other.l[0]*self.l[1]
      r[1] = self.l[1]*other.l[1]
      r = Fraction(r)
      r.cut()
      return r
  def cut(self):
    if self.l[1] < 0:
        self.l[0]*=-1
        self.l[1]*=-1
    if self.l[0]//self.l[1] == self.l[0]/self.l[1]:
      self.l[0] = self.l[0]//self.l[1]
      self.l[1] = 1
      return self.l
    #negative = False
    #if self.l[0] < 0: negative = True
    n = common(dc(abs(self.l[0])), dc(abs(self.l[1])))
    if n == []: return self.l
    m = 1
    for i in n:
      m *= i
    self.l[0] //= m
    self.l[1] //= m
    return self.l
