class Human:
    def __init__(self, name, age):
        self._name = name
        self.age = age
    def my_name(self):
        return f'My name is {self._name}'
petya = Human('Petya', 50)
vanya = Human('Ivan', 33)
print(petya.my_name())
print(vanya.my_name())
PI = 3.13
PI += 1
print(PI)
vanya._name = 'Lana'
print(vanya._name)