import random
import string

def password(name,dob):
  name1 = name[:1].upper()
  name2 = name[1:4].lower()
  dob1 = dob[-2:]

  extras = string.ascii_letters + string.digits
  randompart = ''.join(random.choices(extras,k=4))

  password = name1 + name2 + randompart + dob1

  return password

name = "Fadhil"
dob = "26-08-2004"

print("The generated password is :",password(name,dob))
