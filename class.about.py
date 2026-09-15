'''CLASS
    (1) What is class
    (2) Ordinary vs Static properties
    (3) Special methods
'''

print("==== What is class ====")
# Class - blueprint for an object creation!
# Structure > State | Constructure | Method


class Person():
    # state
    message = "static state property"

    # constructure
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("Class: static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# Ordinary state
print("person1.name:", person1.name)

# Ordinary method
person1.introduce()
person2.say_age()


print("==== Ordinary vs Static properties ====")
# Static state
new_message = Person.message
print("new_message:", new_message)

# Static method
Person.explain()
