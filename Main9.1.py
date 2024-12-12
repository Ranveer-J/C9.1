class student:
    name = "penguin"
    grade = 10


    def introduction(self):
        print("Hello, I am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade ", self.grade)

ob = student()
ob.introduction()
ob.details()