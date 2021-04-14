class Student(object):
    def __init__(self,a,b,c):
        self.first_name=a
        self.last_name=b
        self.programme=c
    def attributes(self):
        student=self.first_name+" "+self.last_name+" "+self.programme
        print(student)
#example
a="Candy"
b="Homes"
c="BMI"
z=Student(a,b,c)
z.attributes()
#
a=input('The first name: ')
b=input('The last name: ')
c=input('The undergraduate programme: ')
z=Student(a,b,c)
z.attributes()