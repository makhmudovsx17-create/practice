''' OBJECTS
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math  # import math > packageni yahlid object ko'rinishida chaqirish
from math import ceil  # from math import ceil > aniq bir method yoki statelarni chaqirish
print("==== What is object ====")
# OBJECT is a special data type that has state and method properties.
# Everything is an object in Python!

print(type('Hello world!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# PARADIGM > Functional programming & Object Orineted Proramming (OOP)
# OPP 4 CONCEPTS > Abstraction | Encapsulation | Polymorphism | Inheritance
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)
