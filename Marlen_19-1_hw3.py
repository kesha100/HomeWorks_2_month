class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def GCD(self, a, b):
        return (self.GCD(b, a % b) if b else a)

    def __add__(self, other):
        znam = self.denumerator  * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator + znam // other.denumerator * other.numerator
        self.numerator = chisl
        self.denumerator = znam

        return Fraction(numerator = self.numerator, denumerator = self.denumerator)


    def __sub__(self, other):
        znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        a = znam // self.denumerator * self.numerator
        b = znam // other.denumerator * other.numerator
        self.numerator = a - b
        self.denumerator = znam

        return Fraction(numerator = self.numerator, denumerator = self.denumerator)


    def __mul__(self, other):
        if self.GCD(self.numerator, other.denumerator) > 1:
            k = self.GCD(self.numerator, other.denumerator)
            self.numerator //= k
            other.denumerator //= k

        if self.GCD(self.denumerator, other.numerator) > 1:
            k = self.GCD(self.denumerator, other.numerator)
            self.denumerator //= k
            other.numerator //= k

        self.numerator *= other.numerator
        self.denumerator *= other.denumerator

        return Fraction(numerator = self.numerator, denumerator = self.denumerator)

    def __floordiv__(self, other):

        n = other.denumerator
        other.denumerator = other.numerator
        other.numerator = n

        if self.GCD(self.numerator, other.denumerator) > 1:
            k = self.GCD(self.numerator, other.denumerator)
            self.numerator //= k
            other.denumerator //= k

        if self.GCD(self.denumerator, other.numerator) > 1:
            k = self.GCD(self.denumerator, other.numerator)
            self.denumerator //= k
            other.numerator //= k

        self.numerator *= other.numerator
        self.denumerator *= other.denumerator

        return Fraction(numerator = self.numerator, denumerator = self.denumerator)

    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"


a = list(map(int, input("Введите знаменатель и числитель первой дроби, в виде ?/?: ").split('/')))
b = list(map(int, input("Введите знаменатель и числитель второй дроби: в виде ?/?: ").split('/')))

num1 = Fraction(a[0], a[1])
num2 = Fraction(b[0], b[1])

print(f"{num1.numerator}/{num1.denumerator} + {num2.numerator}/{num2.denumerator} = {num1 + num2}")
num1 = Fraction(a[0], a[1])
print(f"{num1.numerator}/{num1.denumerator} - {num2.numerator}/{num2.denumerator} = {num1 - num2}")
num1 = Fraction(a[0], a[1])
print(f"{num1.numerator}/{num1.denumerator} * {num2.numerator}/{num2.denumerator} = {num1 * num2}")
num1 = Fraction(a[0], a[1])
print(f"{num1.numerator}/{num1.denumerator} // {num2.numerator}/{num2.denumerator} = {num1 // num2}")