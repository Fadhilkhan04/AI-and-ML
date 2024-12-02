from collections import defaultdict

visited = defaultdict(lambda:False)
jug1 , jug2 , aim = 4,3,2

def waterJug(amt1,amt2):

    if((amt1 == aim and amt2 == 0)or(amt2 == aim and amt1 == 0)):
        print(amt1,amt2)
        return True

    if visited[(amt1,amt2)]:
        return False

    visited[(amt1,amt2)] = True
    print(amt1,amt2)

    return ( waterJug(0,amt2) or waterJug(amt1,0) or waterJug(jug1,amt2) or waterJug(amt1,jug2) or waterJug(amt1+min(amt2,jug1-amt1),amt2-min(amt2,jug1-amt1)) or waterJug(amt1-min(amt1,jug2-amt2),amt2+min(amt1,jug2-amt2)))

print("Steps:")
waterJug(0,0)