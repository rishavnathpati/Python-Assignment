class studentDetails:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def getMarks(self):
        return self.marks

    def getRoll(self):
        return self.roll

    def getName(self):
        return self.name

    def show(self):
        return 'Name: '+self.name+'  Roll: '+str(self.getRoll())+'  Marks: '+str(self.getMarks())


def getHighestMarks(record):
    marks = max([i.getMarks() for i in record])
    flag = True
    for j in record:
        if marks == j.getMarks():
            print("{} got highest marks.".format(j.getName()))
            flag = False
    if flag == True:
        print("Invalid")


def main():
    record = []
    confirmation = 'y'
    while confirmation == 'y':
        name = input("Enter Student Name: ")
        roll = int(input("Enter Student Roll: "))
        marks = int(input("Enter Student Marks: "))
        record.append(studentDetails(name, roll, marks))
        confirmation = input("Want to insert another record?(y/n)")
    for i in record:
        print(i.show())

    getHighestMarks(record)


if __name__ == "__main__":
    main()
