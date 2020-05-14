class stud:
    school="GLA"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getinfo(cls):
        return cls.school
    @staticmethod
    def info():
        print("Gla university")
s1=stud(15,15,30)
s2=stud(45,55,78)
print(s1.avg())
print(s1.getinfo())
stud.info()