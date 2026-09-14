print("==== Iterable objects & RANGE ====")
# Iterable (takrorlanish) objects > string | dict | tuple | list | range | map | filter

range_obj = range(3)  # [0, 3] = (0, 1, 2)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("==== DICTIONARY ====")
# Dictionary = JSON object!
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Jusctin", age=25, single=True)  # Used more often
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# name = person_obj["name"] <==> method.get()
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    # print(f"the key: {key} => {person_obj[key]}") <==> print(f"the key: {key} > {person_obj.get(key)}")
    print(f"the key: {key} > {person_obj.get(key)}")
