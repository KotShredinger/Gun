class Vector:
    def __init__(self, x ='0,0', y = 0):
        if type(x)==str:
            s=x.split(',')
            self.x = float(s[0])
            self.y = float(s[1])
        else:
            self.x = float(x)
            self.y = float(y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
a=Vector('1,2')
b=Vector('2,3')
c=a-b
print(c.x, c.y)
d=Vector(3, 4)
e=a-d
print(e.x, e.y)
