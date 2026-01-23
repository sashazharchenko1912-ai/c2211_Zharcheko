import random

cars = [
    {"brand": "Toyota", "condition": 80, "price": 3000},
    {"brand": "BMW", "condition": 70, "price": 5000},
    {"brand": "Audi", "condition": 75, "price": 4500},
    {"brand": "Volkswagen", "condition": 85, "price": 3500},
    {"brand": "Honda", "condition": 90, "price": 3200}
]

jobs = [
    {"title": "Програміст", "salary": 2000},
    {"title": "Тестувальник", "salary": 1500},
    {"title": "Менеджер", "salary": 1200},
    {"title": "Фрілансер", "salary": 1800}
]

homes = [
    {"type": "Квартира", "price": 8000},
    {"type": "Будинок", "price": 12000}
]

class Student:
    def __init__(self):
        self.name = "Gaben"
        self.street = "Google 10"

        self.job = random.choice(jobs)
        self.car = random.choice(cars).copy()
        self.home = None

        self.hunger = 100
        self.fun = 100
        self.cleanliness = 100
        self.energy = 100
        self.money = 500

        self.goals = {
            "Накопичити 5000$": False,
            "Купити нове авто": False,
            "Чистота дому ≥ 80": False,
            "Енергія ≥ 70 наприкінці року": False,
            "Купити житло": False
        }

    def work(self):
        income = self.job["salary"] // 30
        self.money += income
        self.energy -= 10
        self.hunger -= 10
        self.fun -= 5
        return f"Працював (+{income}$)"

    def go_shop(self):
        if self.money >= 20:
            self.money -= 20
            self.hunger = min(100, self.hunger + 30)
            return "Сходив у магазин (-20$)"
        return "Не вистачило грошей на магазин"

    def clean_house(self):
        self.cleanliness = min(100, self.cleanliness + 30)
        self.energy -= 5
        return "Прибирав у домі"

    def rest(self):
        self.energy = min(100, self.energy + 20)
        self.fun = min(100, self.fun + 10)
        return "Відпочивав"

    def repair_car(self):
        cost = 100
        if self.money >= cost:
            self.money -= cost
            self.car["condition"] = min(100, self.car["condition"] + 30)
            print(f"Ремонт авто (-{cost}$). Баланс: {self.money}$")

    def buy_new_car(self):
        for car in cars:
            if self.money >= car["price"]:
                self.money -= car["price"]
                self.car = car.copy()
                self.goals["Купити нове авто"] = True
                print(f"Куплено нове авто: {car['brand']}")
                break

    def buy_home(self):
        if self.home is None:
            for home in homes:
                if self.money >= home["price"]:
                    self.money -= home["price"]
                    self.home = home
                    self.goals["Купити житло"] = True
                    print(f"Куплено {home['type']} за {home['price']}$")
                    break

    def check_goals(self, day):
        if self.money >= 5000:
            self.goals["Накопичити 5000$"] = True

        if self.cleanliness >= 80:
            self.goals["Чистота дому ≥ 80"] = True

        if day == 365 and self.energy >= 70:
            self.goals["⚡ Енергія ≥ 70 наприкінці року"] = True

    def day_actions(self, day):
        action = random.choice(["work", "shop", "clean", "rest"])

        if action == "work":
            text = self.work()
        elif action == "shop":
            text = self.go_shop()
        elif action == "clean":
            text = self.clean_house()
        else:
            text = self.rest()

        # Знос авто
        self.car["condition"] -= random.randint(0, 2)
        self.car["condition"] = max(0, self.car["condition"])

        if self.car["condition"] <= 30:
            self.repair_car()

        if self.money >= 3000 and not self.goals["Купити нове авто"]:
            self.buy_new_car()

        if self.money >= 8000 and not self.goals["Купити житло"]:
            self.buy_home()

        self.cleanliness -= 1

        self.hunger = max(0, self.hunger)
        self.fun = max(0, self.fun)
        self.energy = max(0, self.energy)

        self.check_goals(day)
        return text

student = Student()

for day in range(1, 366):
    print(f"\nДень {day}")
    action = student.day_actions(day)

    print(f"Дія: {action}")
    print(f"Баланс: {student.money}$")
    print(f"Авто: {student.car['brand']} ({student.car['condition']}%)")
    print(f"Ситість: {student.hunger}")
    print(f"Задоволення: {student.fun}")
    print(f"Чистота дому: {student.cleanliness}")
    print(f"Енергія: {student.energy}")

print("\nПІДСУМОК РОКУ")
print(f"Імʼя студента: {student.name}")
print(f"Адреса: вулиця {student.street}")
print(f"Робота: {student.job['title']}")

if student.home:
    print(f"Житло: {student.home['type']}")
else:
    print("Житло: не придбав")

print("\nВиконані цілі:")
for goal, done in student.goals.items():
    print(f"- {goal}: {'Так' if done else 'Ні'}")
