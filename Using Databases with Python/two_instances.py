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

a = Student('Kedar')
a.std()
a.giveName()
print('--------------------Another Object-------------------')

b=Student('Mandar')
b.giveName()
b.std()
