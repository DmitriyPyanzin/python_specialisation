from lesson10.hw.task4.AnimalFactory import AnimalFactory

dog = AnimalFactory.create_animal('Dog', 'Buddy', 'Golden Retriever')
cat = AnimalFactory.create_animal('Cat', 'Whiskers', 'Black')

print(dog)
print(cat)

print(dog.speak())
print(cat.speak())
