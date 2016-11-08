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
N=int(input())
s=[[0]*2 for i in range(N)]
for i in range(N):
    s[i]= list(map(int, input().split()))
m=Vector(0, 0)
for i in range(N):
    t=Vector(s[i][0], s[i][1])
    m+=t
print(m.x/N, m.y/N)