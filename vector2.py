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
N=int(input())
s=[[0]*2 for i in range(N)]
for i in range(N):
    s[i]= list(map(int, input().split()))
maxn=max(s)
print(maxn)