#water jug problem
def water(jug1_capacity,jug2_capacity,goal_size,target_jug):
    jug1=0
    jug2=0
    steps=0
    while jug1!=goal_size or jug2!=goal_size:
        steps+=1
        if jug1==0:
            print("Step ",steps,"FILL JUG 1 TO CAPACITY ",jug1_capacity)
            jug1=jug1_capacity
        elif jug2==jug2_capacity:
            print("Step ",steps,"EMPTY THE JUG")
            jug2=0
        else:
            transfer=min(jug1,jug2_capacity-jug2)
            jug1-=transfer
            jug2+=transfer
            print("Step ",steps," POUR ",transfer," FROM JUG 1 TO JUG 2")
        if target_jug==jug1:
            if jug1==goal_size:
                break
        else:
            if jug2==goal_size:
                break
    print("GOAL REACHED IN ",steps," STEPS")
jug1_capacity=int(input("ENTER SIZE OF JUG 1 :"))
jug2_capacity=int(input("ENTER SIZE OF JUG 2 :"))
goal_size=int(input("ENTER GOAL SIZE : "))
target_jug=int(input("ENTER TARGET JUG : "))
if target_jug not in [1,2]:
    print("INVALID")
else:
    water(jug1_capacity,jug2_capacity,goal_size,target_jug)
