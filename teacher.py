#Create a Teacher class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

class Teacher:
  def __init__(self, salary, subjects):
    self.subjects = subjects
    self.salary = salary
  def enroll(self, subjects):
    self.subjects.append(subject)
  def info(self, name, salary, subjects):
    print("name:" + name)
    print("salary:" + self.salary)
    print("subjects:", ", ".join(self.subjects))
