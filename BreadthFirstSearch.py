#BREADTH FIRST SEARCH
print("BREADTH FIRST SEARCH")
graph={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
       'F':[],
       'G':[]}
visited=[]
neigh=[]
st=(input("ENTER START NODE : "))
gt=(input("ENTER GOAL NODE : "))
def bfs(graph,st,gt):
    visited.append(st)
    neigh.append(st)
    while neigh:
        key=neigh.pop(0)
        #print(key,"-->",end=' ')
        if gt==key:
            break
        else:
            for neighbor in graph[key]:
                if neighbor not in visited:
                    neigh.append(neighbor)
                    visited.append(neighbor)
bfs(graph,st,gt)
print("PATH : ",end=" ")
print(visited)
