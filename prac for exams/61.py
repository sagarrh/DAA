class calculator:
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        else:
            return a / b
        
calc= calculator()
result=calc.subtract(2,3)
print(result)