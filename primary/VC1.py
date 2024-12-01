def clean(floor,m):
    for i in range(m):
        if( floor[i] == 0):
            print("location ",i+1," is already clean")

        else:
            print("cleaning location ",i+1)
            floor[i] = 0
    print("cleaning done")
    print(floor)



def main():
    floor = []
    m = int(input("enter the number of locations :"))
    for i in range(m):
        print("enter clean(0) dirty(1) for location ", i+1)
        f = int(input())
        floor.append(f)
    print(floor)
    clean(floor,m)

main()