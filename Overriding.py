class parent:
    def mobile(self):
        print("Lenovo k8")
class child:
    def mobile(self):
        print("Iphone 6s")
class smallbrother(parent,child):
    pass

c=smallbrother()
c.mobile()
a=parent()
b=child()
a.mobile()
b.mobile()