class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))
        
def findConnectionLevel(n, Gmat, px, py):
  level={}
  parent={}
  for i in range(n):
    level[i]=0
    parent[i]=-1
  q=Queue()

  level[px]=0
  q.addq(px)

  while(not q.isempty()):
    j= q.delq()
    for k in range(n):
      if (level[k]==0 and Gmat[j][k]==1):
        level[k]=level[j]+1
        parent[k]=j
        q.addq(k)

  return (level[py])
  
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))