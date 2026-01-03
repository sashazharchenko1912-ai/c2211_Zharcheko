class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_person(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


class Worker(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary

    def work(self):
        return f"Працює як {self.job}, зарплата {self.salary} грн"


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def study(self, grade):
        self.grades.append(grade)

    def avg_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0


class WorkingStudent(Worker, Student):
    def __init__(self, name, age, job, salary, university):
        super().__init__(name, age, job, salary)
        self.university = university
        self.grades = []

    def full_info(self):
        return (
            f"{self.info_person()}\n"
            f"{self.work()}\n"
            f"Навчається в: {self.university}\n"
            f"Середній бал: {self.avg_grade()}"
        )


if __name__ == "__main__":
    ws = WorkingStudent(
        name="Gaben",
        age=18,
        job="Програміст",
        salary=15000,
        university="STEP Academy"
    )

    ws.study(10)
    ws.study(11)
    ws.study(12)

    print(ws.full_info())
