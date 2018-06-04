class Car:
    wheels = 4

    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def upgrade(self, new_model):
        self.model = new_model
        self.brand = "Still {}".format(self.brand)


elon = Car("Tesla", "Model X", "Electric")
print(elon.wheels)
print(elon.model)
elon.upgrade("Model 3")
print(elon.model + " " + elon.brand)
