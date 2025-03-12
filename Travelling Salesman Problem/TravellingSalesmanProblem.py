#TRAVELLING SALESMAN
from sys import maxsize
from itertools import permutations
V=5
graph=[[0,9,6,7,10],[9,0,8,11,17],[6,8,0,7,15],[7,11,7,0,6],[10,17,15,6,0]]
s=0
print("TRAVELLING SALESMAN")
def trav(graph,s):
    vertex=[i for i in range(V) if i!=s]
    min_path=maxsize
    min_path_sequence=None
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_path_weight=0
        k=s
        path_sequence=[s]
        for j in i:
            current_path_weight+=graph[k][j]
            k=j
            path_sequence.append(j)
        current_path_weight+=graph[k][s]
        path_sequence.append(s)
        if current_path_weight<min_path:
            min_path=current_path_weight
            min_path_sequence=path_sequence
        print("MINIMUM PATH : ",min_path_sequence)
        return min_path
print("MINIMUM PATH COST: ",trav(graph,s))
