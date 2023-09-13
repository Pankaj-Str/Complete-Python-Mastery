class info:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def PrintData(self):
        print("Your Name is : ",self.name)
        print("Your age is : ",self.age)
        print("Your height is : ",self.height)

    def getName(self):
        return self.name  
    def getAge(self):
        return self.age
    def getHeight(self):
        return self.height   
     
    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def setHeight(self,height):
        self.height = height 

Info = info("joy",12,3.5)
Info.PrintData()
print(Info.getName())
print(Info.getAge())
print(Info.getHeight())

Info.setName("Toy")
Info.PrintData()
