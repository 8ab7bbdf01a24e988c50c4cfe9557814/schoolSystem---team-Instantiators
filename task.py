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
  def getmark(self, student):
    return self.marks.get(student, "No mark found")
  def info(self):
    print(f"This task is '{self.name}' and is out of {self.maxMark} marks.")
  def Max(self):
    return max(self.marks.values()) if self.marks else None
  def Avg(self):
    return sum(self.marks.values()) / len(self.marks) if self.marks else None
  def Min(self):
    return min(self.marks.values()) if self.marks else None
