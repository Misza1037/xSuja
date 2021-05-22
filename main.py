class Polynomial:
  def __init__(self, *args):
    self.args = args
  def __add__(self, other):
    return Polynomial(list(map(sum()), zip(self.args, other.args)))
