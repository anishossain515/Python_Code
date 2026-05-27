class Calculator:
    def __init__(self):
        self.a = int(input('Enter your first number: '))
        self.b = int(input('Enter your second number: '))

    def additon(self):  
        return self.a + self.b
    
    def substraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a // self.b
    
    def __str__(self):
        return f'The addition value of your number : {self.additon()}\nThe substraction value of your number : {self.substraction()}\nThe multiplication value of your number : {self.multiplication()}\nThe division value of your number : {self.division()}'


result = Calculator()
print(result)