class Grade(object):
    def __init__(self,a,b,c,d):
        self.name=a
        self.grade_code=b
        self.grade_poster=c
        self.grade_final=d
    def total_mark(self):
        mark=float(self.grade_code)*0.4+float(self.grade_poster)*0.3+float(self.grade_final)*0.3
        result=a+" "+str(mark)
        print(result)
        return mark,a
#example
a="Candy"
b=90
c=85
d=95
z=Grade(a,b,c,d)
z.total_mark()
#
a=input('Student name: ')
b=input('Student grade for code portfolio: ')
c=input('Student grade for the poster presentation: ')
d=input('Student grade in the final exam: ')
z=Grade(a,b,c,d)
z.total_mark()