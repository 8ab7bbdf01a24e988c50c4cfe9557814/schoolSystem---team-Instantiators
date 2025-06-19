#Create a PrimaryStudent class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

class primaryStudent():
    def __init__(self, name, schoolYear, teacher):
        self.name = name
        self.schoolYear = schoolYear
        self.teacher = teacher

    def setTeacher(self, teacher):
        self.teacher = teacher
    def getTeacher(self, teacher):
        self.teacher = teacher
    def info(self, name, schoolYear, teacher):
        return (f"my name is {self.name}")
