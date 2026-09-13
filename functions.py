''' FUNCTIONS
  (1) DEFINE vs CALL
  (2) Parametr vs Argument
  (3) Keyword & Default arguments
  (4) Scope
'''

print("==== DEFINE (parametr) vs CALL (argument) ====")
# buld in functions > print(), type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet("Martin")
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


print("==== Keyword & Default arguments =====")


# DEFINE
def give_greet(name, age=22):  # age=22 => default argument
    print("give_print is executed")
    return f"Hi {name} you are {age} years old"


# CALL
# name="Justin", age=28 => keyword argument
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)


print("==== Scope ====")
b = 100  # 3


# DEFINE
def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5, 50)
