class House:
    def __init__(self, address):
        self.address = address


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
        print(f"  👔 Працює як {self.job.title}")

    def eat(self, food):
        self.pleasure += food.pleasure
        self.fatigue -= 5
        print(f"  🍔 Їсть {food.name}")

    def rest(self):
        self.fatigue -= 10
        print("  😴 Відпочиває вдома")

    def status(self):
        self.fatigue = max(0, self.fatigue)
        self.pleasure = min(100, self.pleasure)
        print(
            f"  📊 Стан: гроші={self.money}, "
            f"задоволення={self.pleasure}, "
            f"втома={self.fatigue}"
        )


# симуляція 365 днів
if __name__ == "__main__":
    house = House("вул. Google, 10")
    job = Job("Програміст", salary=500, fatigue=10)
    food = Food("піца", pleasure=8)

    person = Person("Gaben")
    person.move_in(house)
    person.get_job(job)

    for day in range(1, 366):
        print(f"\n📅 День {day}")

        person.work()
        person.eat(food)

        if person.fatigue > 40:
            person.rest()

        person.status()
