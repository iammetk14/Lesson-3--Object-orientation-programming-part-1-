class student:
    grade=8
    name="Tejas"
    school="The Shriram Millenium School"
    def introduction(self):
        print("Hi! I am a student in the",self.school)
    def details(self):
        print("My name is",self.name)
        print("I study in grade",self.grade)
ob=student()
ob.introduction()
ob.details()