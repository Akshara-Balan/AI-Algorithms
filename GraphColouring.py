#GRAPH COLOURING
domain=['RED','BLUE','GREEN']
vertices=['1','2','3','4','5']
colors={}
graph={'1':['2'],
        '2':['1','3','4','5'],
        '3':['2'],
        '4':['2','5'],
        '5':['2','3']}
def promise(vertex,dom):
    for neighbor in graph.get(vertex):
        if colors.get(neighbor)==dom:
            return False
    return True
def color_vertex(vertex):
    for dom in domain:
        if promise(vertex,dom):
            return dom
for vertex in vertices:
    colors[vertex]=color_vertex(vertex)
print(colors)
