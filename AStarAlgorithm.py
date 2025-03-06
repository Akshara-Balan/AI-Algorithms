#A* search algorithm
graph={'S':[('A',1),('G',10)],
      'A':[('B',5),('C',1)],
      'B':[('D',5)],
      'C':[('D',3),('G',4)],
      'D':[('G',2)],
      'G':[]}
heurestic={'S':5,'A':3,'B':4,'C':2,'D':6,'G':0}
start='S'
goal='G'
def get_heurestic(node,heurestic):
    return heurestic[node]
def astar(graph,heurestic,start,goal):
    openlist=[]
    closedlist=[]
    path={}
    openlist.append((0,start))
    path[start]=[start]
    while openlist:
        currentnode=min(openlist,key=lambda x:x[0]+get_heurestic(x[1],heurestic))
        if currentnode[1]==goal:
            return path[goal]
        openlist.remove(currentnode)
        closedlist.append(currentnode)
        for node,cost in graph[currentnode[1]]:
            if node not in [x[1] for x in closedlist]:
                    openlist.append((currentnode[0]+cost,node))
                    path[node]=path[currentnode[1]]+[node]
    return None
path=astar(graph,heurestic,start,goal)  
if path is not None:
    print('-->'.join(path))
else:
    print("NO PATH FOUND")
