class Polynomial:
  def __init__(self, *args):
    self.args = args
    self.p = self.args[0]
    self.q = self.args[-1]
    self.p_tab = self.zwroc_dzielniki(self.p)
    self.q_tab = self.zwroc_dzielniki(self.q)
    self.potencjalne_pierwiastki = self.zwroc_ilorazy(self.p_tab, self.q_tab)
    self.pierwiastki = self.zwroc_pierwiastki(self.potencjalne_pierwiastki)
    
  def zwroc_ilorazy(self, P, Q):
    tab = []
    for p, q in zip(P, Q):
      tab.append(p/q)
    return tab
  
  def zwroc_dzielniki(self, a):
    tab = []
    for i in range(1, a//2 + 1):
      if a % i == 0: tab.append(i)
    return tab
  
  def zwroc_pierwiastki(self, a):
    tab = []
    for x in a:
      if f(x) == 0:
        tab.append(x)
    return tab
  
  def f(self, x):
        sum = 0
        for a in range(len(self.args)):
            sum += x**a * self.args[a]
        return sum

a = Polynomial([0, 0, 1])
