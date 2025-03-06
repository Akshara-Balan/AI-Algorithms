#DEPTH FIRST SEARCH
print("DEPTH FIRST SEARCH")
graph={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
       'E':[],
      'F':[],
      'G':[]}
visited=[]
frontier=[]
st=input("ENTER STARTING NODE : ")
gt=input("ENTER GOAL NODE : ")
def dfs(graph,st,gt):
    visited.append(st)
    frontier.append(st)
    while frontier:
        key=frontier.pop()
        print(key)
        if key==gt:
            break
        else:
            for neighbor in graph[key]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    frontier.append(neighbor)
dfs(graph,st,gt)     
