from collections import defaultdict

jug1, jug2, aim = 4, 3, 2  # capacities of the jugs and the target amount
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2): 
    # Base condition: if either jug contains the target amount and the other jug is empty
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True

    if visited[(amt1, amt2)]:
        return False

    # Mark this state as visited
    visited[(amt1, amt2)] = True
    print(amt1, amt2)
    
    # Recursive calls for all possible actions
    return (
        waterJugSolver(0, amt2) or         # Empty jug1
        waterJugSolver(amt1, 0) or         # Empty jug2
        waterJugSolver(jug1, amt2) or      # Fill jug1
        waterJugSolver(amt1, jug2) or      # Fill jug2
        waterJugSolver(amt1 + min(amt2, jug1 - amt1), amt2 - min(amt2, jug1 - amt1)) or  # Pour from jug2 to jug1
        waterJugSolver(amt1 - min(amt1, jug2 - amt2), amt2 + min(amt1, jug2 - amt2))       # Pour from jug1 to jug2
    )

print("Steps:")
waterJugSolver(0, 0)