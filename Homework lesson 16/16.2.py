class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return Fraction(self.a * other, self.b)

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.a * other.b + other.a * self.b,
                self.b * other.b
            )
        return Fraction(self.a + other * self.b, self.b)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.a * other.b - other.a * self.b,
                self.b * other.b
            )
        return Fraction(self.a - other * self.b, self.b)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return self.a == other * self.b

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return self.a > other * self.b

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return self.a < other * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"