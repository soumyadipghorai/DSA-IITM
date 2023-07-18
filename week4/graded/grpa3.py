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


def longJourney(AList):
  indegree={}
  lpath={}
  parent={}
  l=[]
  zerodegreeq = Queue()


  for u in AList.keys():
    (indegree[u],lpath[u],parent[u]) = (0,0,None)
    
  for u in AList.keys():
    for v in AList[u]:
      indegree[v] = indegree[v] + 1

  for u in AList.keys():
    if indegree[u] == 0:
      zerodegreeq.addq(u)
      parent[u]

  while (not zerodegreeq.isempty()):
    j = zerodegreeq.delq()
    indegree[j] = indegree[j]-1
    for k in AList[j]:
      parent[k]=j
      indegree[k] = indegree[k] - 1
      lpath[k] = max(lpath[k],lpath[j]+1)
      if indegree[k] == 0:
        zerodegreeq.addq(k)
  
             
  while not(k==None):
    l.append(k)
    k=parent[k]
  
  l.reverse()
  return (l)
