from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    # name: str
    name: str = "Nikhil"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10, default=5, description="A decimal value representing the cgpa of the student")

# new_student = {'name': 'Nikhil'}
# new_student = {'name': 26}
# new_student = {}
# new_student = {'age': 26}
# new_student = {'age': '26'}
# new_student = {'age': '26', 'email': 'abc'}
# new_student = {'age': '26', 'email': 'abc@gmail.com'}
# new_student = {'age': '26', 'email': 'abc@gmail.com', 'cgpa': 12}
# new_student = {'age': '26', 'email': 'abc@gmail.com', 'cgpa': 8.4}
new_student = {'age': '26', 'email': 'abc@gmail.com'}

student = Student(**new_student)

print(student)
print(type(student))
print(student.name)
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()