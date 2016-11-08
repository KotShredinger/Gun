class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+','+str(self.y)
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    def __lt__(self,other):
        return (self.x**2+self.y**2)<(other.x**2+other.y**2)
N=int(input())
s=[]
for i in range(N):
    x1,y1=list(map(float,input().split(',')))
    a=vector(x1,y1)
    s.append(a)

maxn=max(s)
print(maxn)