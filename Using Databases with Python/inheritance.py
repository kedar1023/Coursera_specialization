class Student:
    x = 0
    student_name=''
    def std(kedar):
            kedar.x=kedar.x+1
            print('Value of ',kedar.x)


    def __init__(self,name):
            self.student_name=name
            print("Call to constructor :)")

    def giveName(self):
        print('My Name is',self.student_name)



class child(Student):
    points=0
    def extraOne(self):
            self.points=self.points+1023
            self.giveName()
            print('Value of Points',self.points)


a = Student('Kedar')
a.std()
a.giveName()
print('--------------------Another use ofInheritence-------------------')

b=child('Mandar')
b.extraOne()
b.giveName()
print(dir(b))

