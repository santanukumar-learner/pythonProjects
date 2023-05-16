'''
def formated(f_name, l_name):
    a = f_name.title()
    b = l_name.title()
    return f"{a} {b}"
print(formated(input("What is your first name? "), input("What is your last name? ")))
'''
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

    # 🚨 Do NOT change any of the code below


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''

#calculator using function
def sum(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def devide(n1, n2):
    return n1 / n2
def subtract(n1, n2):
    return n1 - n2
operation = {
    "+" : sum, "-" : subtract, "/" : devide, "*" : multiply }
for operator in operation:
    print(operator)
def calculator():
    n1 = float(input("Enter a number: "))
    should_continue = True
    while should_continue:
      operator = input("Choose a operator from above: ")
      n2 = float(input("Enter another number: "))
      calculate = operation[operator]
      result = calculate(n1, n2)
      print(f"{n1} {operator} {n2} = {result}")
      if input(f"you want to continue with {result} yes or no ") == "yes":
          n1 = result
          operator_2 = input("Choose a operator from above again: ")
          n3 = float(input("choose a number again: "))
          calculate_2 = operation[operator_2]
          result_2 = calculate_2(result, n3)
          print(f"{n1} {operator_2} {n3} = {result_2}")
      else:
          should_continue = False
          calculator()
calculator()