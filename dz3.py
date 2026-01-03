class House:
    def __init__(self, address):
        self.address = address

    def info(self):
        return f"Будинок за адресою: {self.address}"


class Person:
    def __init__(self, name):
        self.name = name
        self.house = None

    def move_in(self, house):
        self.house = house

    def info(self):
        if self.house:
            return f"{self.name} живе в будинку за адресою {self.house.address}"
        else:
            return f"{self.name} не має житла"


if __name__ == "__main__":
    house = House("вул. Google, 10")
    person = Person("Gaben")

    person.move_in(house)

    print(house.info())
    print(person.info())
