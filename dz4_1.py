class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Worker(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary

    def work_info(self):
        return f"Works as {self.job}, salary {self.salary}$"


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def study(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0


class WorkingStudent(Worker, Student):
    def __init__(self, name, age, job, salary, university):
        super().__init__(name, age, job, salary)
        self.university = university
        self.grades = []

    def full_info(self):
        return (
            f"{self.person_info()}\n"
            f"{self.work_info()}\n"
            f"Studies at: {self.university}\n"
            f"Average grade: {self.average_grade()}"
        )


# example usage
if __name__ == "__main__":
    ws = WorkingStudent(
        name="Gaben",
        age=18,
        job="Programmer",
        salary=1500,
        university="STEP Academy"
    )

    ws.study(85)
    ws.study(90)
    ws.study(95)

    print(ws.full_info())
