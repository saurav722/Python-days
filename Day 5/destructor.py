class A:  
    
    #  we will initialize the class  
    def _init_(self):  
        print(' The class called A is CREATED.')  
class B:  
    def _init_(self, c):  
        self.c = c  
class C:  
    def _init_(self):  
        self.b = B(self)  
    def _del_(self):  
        print("C is deleted")  
def function():  
    c = C()  
    
function()