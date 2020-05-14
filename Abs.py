from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("its a Laptop process")


class Whiteboard(Computer):
    def write(self):
        print("its writing")
    def process(self):
        print("its a wb process")
class Programmer:
    def coding(self,com):
        print("remove bugs")
        com.process()

l=Laptop()
com2=Programmer()
cpm3=Whiteboard()
com2.coding(l)
com2.coding(cpm3)

