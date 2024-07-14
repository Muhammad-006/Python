import art
print(art.logo)
def addition(n1, n2):
  return n1 + n2
def subtraction(n1, n2):
  return n1 - n2
def multiplication(n1, n2):
  return n1 * n2
def division(n1, n2):
  if n2 == 0:
    return 
  return n1 / n2

operators = {
  '+' : addition,
  '-' : subtraction,
  '*' : multiplication,
  '/' : division
}
inner_check ='new'  
check = 'start'
while check != 'end':
  if inner_check == 'new': 
    num1 = int(input('What is the first number? '))
    num2 = int(input('What is the second number? '))
  elif inner_check == 'yes':
    num1 = result 
    num2 = int(input('What is the number you want to continue the calculation with? '))
  for i in operators:
    print(i)
  symbol = input("Chose the operation you want to perform: ")
  if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
    print("You entered a wrong choice!")
    continue
  function = operators[symbol]
  result = function(num1,num2)
  print(f"{num1} {symbol} {num2} = {result}")
  check = input("Type 'end' to shut the calculator down, Otherwise Type 'no': ").lower()
  if check != 'end':
    inner_check = input(f"Type 'yes' to continue calculation with {result}, Otherwise press 'new' for new calculation: ").lower()
print("GOOD BYE!") 