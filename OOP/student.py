
class Student:
    school="Akirachix"
    
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name=first_name
        self.last_name=last_name
        self.code=code
        self.age=age
        self.country=country
        
    def  greet_student(self):
        greeting=f"Hello{self.first_name},welcome to{self.school}.your code is {self.code}"
        return greeting
    
    
    def year_of_birth(self):
        return f"Hello{self.first_name},you were bornin{2024-self.age}"
    
        