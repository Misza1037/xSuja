class Polynomial:
  def __init__(self, *args):
    self.args = args
  def __add__(self, other):
    return Polynomial(list(map(sum()), zip(self.args, other.args)))
  
  def f(self, x):
        sum = 0
        for a in range(len(self.args)):
            sum += x**a * self.args[a]
        return sum

a = Polynomial([0, 0, 1])
