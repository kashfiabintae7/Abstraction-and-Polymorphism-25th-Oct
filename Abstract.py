from abc import ABC, abstractmethod

class Absclass(ABC):
    
    def print(self,x):
        print("passed Value:", x)
        
    @abstractmethod
    def task(self):
        print("We are insideAbsclass task:")
        
class testClass(Absclass):
    def task(self):
        print("We are insidetest_class task")
        
        
testObj = testClass()
testObj.task()
testObj.print(100)


