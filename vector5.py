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
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y
    def area(self, other, other2):
        return ((self.x - other2.x )*(other.y - other2.y )-(other.x - other2.x )*(self.y - other2.y ))/2
N=int(input())
s=[[0]*2 for i in range(N)]
for i in range(N):
    s[i]= list(map(float, input().split()))
m=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i.area(j,k) > m:
                m = i.area(j,k)
print(m)
