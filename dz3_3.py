import random


class House:
    def __init__(self, address):
        self.address = address
        self.cleanliness = 100

    def clean(self):
        self.cleanliness = 100
        print("Cleaning the house")


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
        self.pleasure = 50
        self.fatigue = 0

    def move_in(self, house):
        self.house = house

    def get_job(self, job):
        self.job = job

    def work(self):
        self.money += self.job.salary
        self.fatigue += self.job.fatigue
        self.pleasure -= 2
        print(f"Working as {self.job.title}")

    def eat(self, food):
        self.pleasure += food.pleasure
        self.fatigue -= 5
        print(f"Eating {food.name}")

    def rest(self):
        self.fatigue -= 10
        print("Resting")

    def clean_house(self):
        self.house.clean()
        self.fatigue += 5
        self.pleasure += 3

    def status(self):
        self.fatigue = max(0, self.fatigue)
        self.pleasure = max(0, min(100, self.pleasure))
        self.house.cleanliness -= 5

        print(
            f"Money: {self.money}, "
            f"Pleasure: {self.pleasure}, "
            f"Fatigue: {self.fatigue}, "
            f"Cleanliness: {self.house.cleanliness}"
        )



if __name__ == "__main__":
    house = House("Google street, 10")
    job = Job("Programmer", salary=500, fatigue=10)

    foods = [
        Food("Pizza", 8),
        Food("Burger", 6),
        Food("Salad", 4),
        Food("Apple", 2)
    ]

    person = Person("Gaben")
    person.move_in(house)
    person.get_job(job)

    for day in range(1, 366):
        print(f"\nDay {day}")

        person.work()

        food = random.choice(foods)
        person.eat(food)

        if person.fatigue > 40:
            person.rest()

        if person.house.cleanliness < 40:
            person.clean_house()

        person.status()
