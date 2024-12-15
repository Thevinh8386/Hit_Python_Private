class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def countDoctor(self):
        dem = 0
        for person in self.people:
            if isinstance(person, Doctor):
                dem += 1
        return dem

    def getYearOfBirth(self, person):
        return person.yob

    def sortAge(self):
        self.people.sort(key=self.getYearOfBirth)

    def aveTeacherYearOfBirth(self):
        total_yob = 0
        dem = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total_yob += person.yob
                dem += 1
        if dem == 0:
            return 0
        return total_yob / dem

# Tạo đối tượng cho Student, Teacher, và Doctor
student1 = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
teacher2 = Teacher("teacherB", 1995, "History")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")

# Tạo Ward và thêm người vào
ward1 = Ward("Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)

print("Thông tin của Ward và mọi người: ")
ward1.describe()

# Đếm số lượng Doctor
print("\nSố lượng bác sĩ:", ward1.countDoctor())

# Sắp xếp theo tuổi và in
print("\nSau khi sắp xếp theo tuổi:")
ward1.sortAge()
ward1.describe()

# TB nsinh của giáo viên
print("\nTB năm sinh của giác viên:", ward1.aveTeacherYearOfBirth())
