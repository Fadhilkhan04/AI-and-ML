import random
import string

def password(length):
  if length < 4:
    return "Password must be minimum of length 4"

  upper = string.ascii_uppercase
  lower = string.ascii_lowercase
  digits = string.digits
  extras = string.punctuation

  password = [random.choice(upper),random.choice(lower),random.choice(digits),random.choice(extras)]

  everything = upper + lower + digits + extras
  password += random.choices(everything,k=length-4)

  random.shuffle(password)

  return ''.join(password)

length = int(input("Enter the length of the password :"))
print("The generated password is :",password(length))
