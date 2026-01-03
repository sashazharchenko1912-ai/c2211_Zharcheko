import random


class House:
    def __init__(self, address):
        self.address = address
        self.cleanliness = 100

    def clean(self):
        self.cleanliness = 100
        print("Прибирання в домі")


class Food:
    def __init__(self, name, pleasure):
        self.name = name
        self.pleasure = pleasure


class Job:
    def __init__(self, title, salary, fatigue):
        self.title = title
        self.salary = salary
        self.fatigue = fatigue


class Person:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.job = None
        self.money = 0
        self.zadovolennia = 50
        self.vtoma = 0

    def move_in(self, house):
        self.house = house

    def get_job(self, job):
        self.job = job

    def work(self):
        self.money += self.job.salary
        self.vtoma += self.job.fatigue
        self.zadovolennia -= 2
        print(f"Працює як {self.job.title}")

    def eat(self, food):
        self.zadovolennia += food.pleasure
        self.vtoma -= 5
        print(f"Їсть {food.name}")

    def rest(self):
        self.vtoma -= 10
        print("Відпочиває")

    def clean_house(self):
        self.house.clean()
        self.vtoma += 5
        self.zadovolennia += 3

    def status(self):
        self.vtoma = max(0, self.vtoma)
        self.zadovolennia = max(0, min(100, self.zadovolennia))
        self.house.cleanliness -= 5

        print(
            f"Гроші: {self.money}, "
            f"Задоволення: {self.zadovolennia}, "
            f"Втома: {self.vtoma}, "
            f"Чистота дому: {self.house.cleanliness}"
        )


# симуляція 365 днів
if __name__ == "__main__":
    house = House("вул. Google, 10")
    job = Job("Програміст", salary=500, fatigue=10)

    foods = [
        Food("Піца", 8),
        Food("Бургер", 6),
        Food("Салат", 4),
        Food("Яблуко", 2)
    ]

    person = Person("Gaben")
    person.move_in(house)
    person.get_job(job)

    for day in range(1, 366):
        print(f"\nДень {day}")

        person.work()

        food = random.choice(foods)
        person.eat(food)

        if person.vtoma > 40:
            person.rest()

        if person.house.cleanliness < 40:
            person.clean_house()

        person.status()
