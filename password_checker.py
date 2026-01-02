def cheak_strenth(password):
  if len(password) < 6:
    return "Weak"
  elif password.isalpha() or password.isdigit():
      return "Medium"
  else:
        return "Strong"

pwd = input("Enter password: ")
result = cheak_strenth(pwd)
print("password strenth: ",result)        