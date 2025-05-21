#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, info):
        self.info = info
        self.knowledge.append(self.info)

student1 = Student('Filla', "Amedi")
student1.learn('Python')
student2 = Student('rilla', "Amedi")
student2.learn('Javascript')
print(student2.knowledge)