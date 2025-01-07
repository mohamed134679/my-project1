class Student:
    def __init__(self, name, age, gender, major, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.id = id

    def dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "major": self.major,
            "id": self.id,
        }
