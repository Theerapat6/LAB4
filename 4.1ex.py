
pi = 3.14

class cylind():
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height

    def cal(self):
        
        cylin = pi*self.Radius**2*self.Height
        return cylin

cylin1 = cylind(5,10)
cylin2 = cylind(7,13)

print(cylin1.cal())
print(cylin2.cal())