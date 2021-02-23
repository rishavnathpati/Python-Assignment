class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("P")

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


class Section():
    def __init__(self, section):
        self.section = section
        print("Sec")

    def printsection(self):
        print(self.section)


class Student(Section, Person):
    def __init__(self, fname, lname, sec):
        self.firstname = fname
        self.lastname = lname
        self.sec1 = sec
        print("S")
        super().__init__(sec)
        Person.__init__(self, fname, lname)

    def printfirst(self):
        print(self.firstname)


x = Student("Mike", "Olsen", "A")
x.printname()
x.printfirst()
x.printsection()
