class Underage(Exception):
    def __init__(self, age):
        super().__init__(f"The age {age} is underage")

def validate(age):
    if age < 18:
        raise Underage(age)
    else:
        print("Age is valid")

try:
    age = int(input("Enter your age: "))
    validate(age)
except ValueError:
    print("Invalid input. Please enter a valid age.")
except Underage as e:
    print(e)
