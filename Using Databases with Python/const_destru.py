class Partyanimal:
    x = 0 
    def animal(kedar):
            kedar.x=kedar.x+1
            print('Value of ',kedar.x)


    def __init__(self):
            print("Call to constructor :)")


    def __del__(self):  
            print("call to Desstructor")       
a = Partyanimal()
a.animal()
a=40 #automatically refere to another object
print(a)