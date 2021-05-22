import fraction

class Polynomial:
    def __init__(self, args):
        self.args = args
        self.p = self.args[0]
        self.q = self.args[-1]
        self.p_tab = self.zwroc_dzielniki(self.p)
        self.q_tab = self.zwroc_dzielniki(self.q)
        self.potencjalne_pierwiastki = self.zwroc_ilorazy(self.p_tab, self.q_tab)
        self.pierwiastki = self.zwroc_pierwiastki(self.potencjalne_pierwiastki)
    def __len__(self):
        return len(self.args)
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


#a = Polynomial([-1, 0, 4])
#print(a.pierwiastki)

X = fraction.Fraction([-4, 2])
Y = fraction.Fraction([1, 3])
testSet = [
[[1,2],[3,4]],
[[-5,6],[8,18]]
]
from random import randint as rand
for i in range(100000):
    tC = [[rand(-10,10), rand(-10,10)],[rand(-10,10), rand(-10,10)]]
    if tC[0][1] != 0 and tC[1][0] != 0 and tC[1][1] != 0:
      testSet.append(tC)
for testCase in testSet:
    test = [fraction.Fraction(testCase[0]), fraction.Fraction(testCase[1])]
    expected = test[0].eval()/test[1].eval()
    result   = (test[0]/test[1]).eval()
    if abs(expected - result)>.0001:
        print(test[0])
        print(test[1])
        print()
#works for:
#1/2, 1/3
#-1/2, 1/3
