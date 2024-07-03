class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        # Add real parts
        real_sum = self.real + other.real
        # Add imaginary parts
        imaginary_sum = self.imaginary + other.imaginary
        return Complex(real_sum, imaginary_sum)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Example usage
c1 = Complex(3, 4)  # Create a complex number with real part 3 and imaginary part 4
c2 = Complex(2, -5)  # Create another complex number with real part 2 and imaginary part -5

result = c1.add(c2)

print("Addition of real part:", result.real)
print("Addition of imaginary part:", result.imaginary)
print("Result:", result)
