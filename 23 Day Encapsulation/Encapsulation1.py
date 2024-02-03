class clientInfo:
    def info(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getheight(self):
        return self.height        
    
C_Info = clientInfo()
C_Info.info("joy",12,3.4)
print("My Name is ",C_Info.getname())
print("My age is ",C_Info.getage())
print("My height is ",C_Info.getheight())
