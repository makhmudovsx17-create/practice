print("==== numbers ====")

# in JAVA, variable is a name of the storage location!
# in PYTHON, variable is a name of the reference!

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1,  result2)
