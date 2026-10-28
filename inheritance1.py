# Inheritance (kalitim) : Miras alma 
#person => eat(),run(),age name , lastname
#student(person),teacher(student)

# animal => dog(animal),cat(animal)

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")
        #print("Person created")

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self, fname, lname)
        #print("Student created")
    def who_am_i(self):
        print("I am a student")
p1 = Person("ali", "yilmaz")
s1 = Student("cınar","turan")

print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " + s1.lastname)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()