while True:
  password = input("Enter a new password: ")

  # Check length
  if not (8 <= len(password) <= 15):
    print("Password must be between 8 and 15 characters long.")
    continue

  # Check for lowercase, uppercase, and numeric characters
  has_lowercase = False
  has_uppercase = False
  has_numeric = False
  for char in password:
    ascii_value = ord(char)
    if 97 <= ascii_value <= 122:  # Lowercase letters
      has_lowercase = True
    elif 65 <= ascii_value <= 90:  # Uppercase letters
      has_uppercase = True
    elif 48 <= ascii_value <= 57:  # Numeric characters
      has_numeric = True

  if not has_lowercase or not has_uppercase or not has_numeric:
    print("Password must contain at least one lowercase, one uppercase, and one numeric character.")
    continue

  print("Password is valid.")
  break