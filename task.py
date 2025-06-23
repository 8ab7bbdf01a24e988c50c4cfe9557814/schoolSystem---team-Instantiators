#Create a Task class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

class Task:
  def __init__(self, name, maxMark, marks):
    self.name = name
    self.maxMark = maxMark
    self.marks = {}
  def setmark(self, student, mark):
    self.marks[student] = mark 
  def getmark(self, mark):
    return self.mark
  def info(self, name):
    print(f"This task is " + self.name)
  def Max(self, marks):
    highest = max(marks)
  def Avg(self, marks):
    median = sum(marks) / len(marks)
  def Min(self, marks):
    lowest = min(marks)
