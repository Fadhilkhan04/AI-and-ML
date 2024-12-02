import time

def clean(house,rooms):
  print("Cleaning started.....")
  time.sleep(1)
  for i in range(rooms):
    if house[i] == 0:
      print("Room ",i+1," is already clean.")
      time.sleep(1)
      if i+1 < rooms:
        print("Moving to Room ",i+2)
        time.sleep(1)

    else:
      print("Cleaning room ",i+1)
      time.sleep(1)
      house[i] = 0
      print("Room ",i+1,"Cleaned")
      time.sleep(1)
      if i+1 < rooms:
        print("Moving to Room ",i+2)
        time.sleep(1)

  print("Cleaning Done....")

def main():
  house = []
  rooms = int(input("Enter the total number of rooms you want to clean :"))
  for i in range(rooms):
    print("Enter the status of room ",i+1," clean(0) or dirty(1) :")
    f = int(input())
    house.append(f)

  clean(house,rooms)

main()