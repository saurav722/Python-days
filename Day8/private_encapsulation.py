class Base:
    def _init_(self):
        self.a = "2"
        self.__c = "3"
 
# Creating a derived class
class Derived(Base):
    def _init_(self):
 
        # Calling constructor of
        # Base class
        Base._init_(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)