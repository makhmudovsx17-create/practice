# Dunder: __builtins__, __init__

message = "PYTHON: Eberything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Puthon, there are builtin tools: 
 (1) TYPES > int, float, str, list, dict
 (2) FUNCTIONS > print(), len(), inpuy(), type() str() int()
 (3) CONSTANTS > True, False, None 
'''

print(dir(__builtins__))
