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
