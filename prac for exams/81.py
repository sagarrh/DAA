import numpy as np

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


values = np.array([0, 12, 45.21, 34, 99.91])

celcuis=values
fahrenheit=np.vectorize(celsius_to_fahrenheit)(celcuis)
print(fahrenheit)