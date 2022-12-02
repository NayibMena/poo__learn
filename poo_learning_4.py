'''Operator Overloading'''
class fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def imprime(self):
        print('{',self.num,'/',self.den,'}')
    def __mul__(self, b):
        n = self.num * b.num
        d = self.den * b.den
        return fraccion(n,d)

a = fraccion(3,7)
b = fraccion(4,9)
c = a*b #nueva definición para el operador '*' dada por el método __mul__
c.imprime()