from __future__ import division
import math

class Rational:
    def __init__(self, numer, denom):
        computedGcd = math.gcd(int(numer), int(denom))
        self.numer = numer / computedGcd
        self.denom = denom / computedGcd
        if self.numer < 0 and self.denom < 0:
            self.numer = abs(self.numer)
            self.denom = abs(self.denom)

        elif self.denom < 0:
            self.numer = self.numer * -1
            self.denom = self.denom * -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)


    def __add__(self, other):
        return Rational(
            (self.numer * other.denom + self.denom * other.numer),
            (self.denom * other.denom)
        )

    def __sub__(self, other):
        return Rational(
            (self.numer * other.denom - self.denom * other.numer),
            (self.denom * other.denom)
        )

    def __mul__(self, other):
        return Rational(
            (self.numer * other.numer),
            (self.denom * other.denom)
        )

    def __truediv__(self, other):
        return  Rational(
            (self.numer  * other.denom),
            (self.denom * other.numer)
        )

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if(power >= 0):
                return Rational(self.numer**power, self.denom**power)
            return Rational(self.denom**abs(power), self.numer**abs(power))
        elif isinstance(power, float):
            return self.numer**power / self.denom**power
    
    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)