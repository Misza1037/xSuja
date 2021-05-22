class Polynomial:
    def __init__(self, args):
        self.args = args
        self.p = self.args[0]
        self.q = self.args[-1]
        self.p_tab = self.zwroc_dzielniki(self.p)
        self.q_tab = self.zwroc_dzielniki(self.q)
        self.potencjalne_pierwiastki = self.zwroc_ilorazy(self.p_tab, self.q_tab)
        self.pierwiastki = self.zwroc_pierwiastki(self.potencjalne_pierwiastki)

    def zwroc_ilorazy(self, P, Q):
        tab = []
        print(P)
        print(Q)
        for p in P:
            for q in Q:
                tab.append(p / q)
        return tab

    def zwroc_dzielniki(self, a):
        tab = []
        if a < 0:
            for i in range(a // 2 - 1, 0):
                if a % i == 0: tab.append(i)
        elif a > 0:
            for i in range(1, a // 2 + 2):
                if a % i == 0: tab.append(i)
        return tab

    def zwroc_pierwiastki(self, a):
        tab = []
        for x in a:
            if self.f(x) == 0:
                tab.append(x)
                tab.append(-x)
        return tab

    def f(self, x):
        sum = 0
        for a in range(len(self.args)):
            sum += x ** a * self.args[a]
        return sum


a = Polynomial([-1, 0, 4])
print(a.pierwiastki)
