class House:
    def __init__(self, address):
        self.address = address

    def info(self):
        return f"Будинок: {self.address}"


class Food:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"Їсть {self.name}"


class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def work(self):
        return f"Працює як {self.title} та заробляє {self.salary} грн"


class Person:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.job = None

    def move_in(self, house):
        self.house = house

    def get_job(self, job):
        self.job = job

    def eat(self, food):
        print(f"{self.name} {food.eat()}")

    def info(self):
        info = f"Імʼя: {self.name}\n"

        if self.house:
            info += f"Житло: {self.house.address}\n"
        else:
            info += "Житло: немає\n"

        if self.job:
            info += f"Робота: {self.job.title}\n"
        else:
            info += "Робота: немає\n"

        return info



if __name__ == "__main__":
    house = House("вул. Google, 10")
    job = Job("Програміст", 30000)
    food = Food("піца")

    person = Person("Gaben")

    person.move_in(house)
    person.get_job(job)

    print(person.info())
    print(job.work())
    person.eat(food)
