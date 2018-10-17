login_types = ["Admin", "Moderator", "user", "guest"]
def gatekeeper(login, account_age):
  if login == "Admin" or "Moderator":
    return "You Have all Access"
  elif login == "user" and account_age <= 7:
      return "You Have Have Some access."
  elif login == "guest":
      return "You Have No Privileges."
account_age=7
print(gatekeeper("guest", account_age))

# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.

# 5. Complete the function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
# 6. If loan_balance is zero or more, it says “you don’t owe any money”
# 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
    return

# 8. Call your function with a negative and positive number and print what it returns.
print(check_balance(300))
