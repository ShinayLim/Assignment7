import re

while True:
  user_input = input("Enter a password : ")
  is_valid = False

  if ((len(user_input) < 8 or len(user_input) > 15)):
    print("Invalid password! It should contain 8-15 characters.")
    continue

  elif not re.search("[A-Z]",user_input):
    print("Invalid password! It should contain atleast one capital letter [A-Z]")
    continue

  elif not re.search("[a-z]",user_input):
    print("Invalid password! It should contain atleast one lowercase letter [a-z]")
    continue

  elif not re.search("[1-9]",user_input):
    print("Invalid password! It should contain one number between [1-9]")
    continue

  elif not re.search("[!@#$%^&*()_+ etc]",user_input):
    print("Invalid password! It should contain at least one special character in [!@#$%^&*()_+ etc]")
    continue

  elif re.search("[\s]",user_input):
    print("Invalid password! It should not contain any space")
    continue

  else:
    is_valid = True
    break

if(is_valid):
  print("Your password is valid!")