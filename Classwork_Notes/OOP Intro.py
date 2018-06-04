class Dog:
    def __init__(self, breed):
        self.breed = breed


doggo = Dog(breed='lab')
print(type(doggo))
print(doggo.breed)
