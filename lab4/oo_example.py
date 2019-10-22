class Triangle:
    height = 10
    base   = 10
    def area(self):
       return 0.5 * self.height * self.base  

    def __len__(self):
        return len("kkkk")
    
    def __str__(self):
        return f"Triangle: Height = {self.height} Base = {self.base} Area: {self.area()} "

# (super - self) 

# overriding parent-child/super-sub

class Person:
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return f"I am a person, my name is {self._name}"
    
    def hello(self): 
        print("Hi, I am a person!")

class Student(Person):
    def __init__(self, name, number):
        super().__init__( name )
        self._number = number
        
    def __str__(self):
        return f"I am a student, my name is {self._name} and my my number is {self._number}"
    
    def hello(self, greeting = ""): 
        if greeting  :
            print(f"{greeting}, I am a student!")
        else:
            super().hello()
            


x = ""

if x : print ("X is not empty") 
else: print("X is empty")

t1 = Triangle()
print( str( t1 ) )
print( "Len : ", len( t1 ))

p1 = Person( "John Doe")
print (p1.__str__())


s1 = Student( "John Doe", 1000)
print( str(s1))

s1.hello()
s1.hello("Hello")


