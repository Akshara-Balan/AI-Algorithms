#tower of hanoi
def toh(n,source,destination,auxiliary):
    if n==1:
        print("MOVE DISK 1 FROM ",source," TO ",destination)
    else:
        toh(n-1,source,auxiliary,destination)
        print('MOVE DISK',n,"FROM ",source,"TO",destination)
        toh(n-1,auxiliary,destination,source)
n=int(input("ENTER NUMBER OF DISKS : "))
toh(n,'S','D','A')
