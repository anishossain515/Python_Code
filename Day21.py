class Result:
    def __init__(self,name,section,roll,grade):
        self.__name = name
        self.__section = section
        self.__roll = roll
        self.grade = grade
    
    def __str__(self):
        return f"{self.__name}({self.__section }-{self.__roll}):{self.grade}"
    
    def get_NSR(self):#to get the private name,section and roll outside (getter method)
        return f"{self.__section}"
    
    def set_Sec(self,section):#to change the private value (setter method)
        if isinstance(section,str) and section.strip() != "":
            self.__section = section
        else:
            print("Must use a valid word")


s1 = Result('Ismail','Sc',25082,'A+')
s2 = Result('Bijoy','Sc',25083,'A-')
s2.grade = 'A+'
s3 = Result('Mahib','Sc',25084,'A+')
s4 = Result('Labir','',25085,'A+')
s4.set_Sec('Sc')

print(s1.get_NSR())
print(s2)
print(s3)
print(s4.get_NSR())



class Car:
    def __init__(self,brand):
        self.brand = brand
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = 'Off'
        
        def start(self):
            self.status = 'Running'

    def drive(self):
        if self.engine.status =='Running':
            print(f'Driving the {self.brand}')
        else:
            print('Start the engine first')
        
d1 = Car('Ferary')
d1.drive()
d1.engine.start()
d1.drive()

        