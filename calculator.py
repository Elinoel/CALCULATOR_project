#this is a calculator programme
number_1 = eval(input("Enter first number: "))
number_2 = eval(input("Enter second number: "))
operator = input("Enter the operator: ")

def add(number_1, number_2):
    result = number_1 + number_2
    return result

def subtract(number_1, number_2):
    result = number_1 - number_2
    return result

def divide(number_1, number_2):
    result = number_1 / number_2
    return result

def multiply(number_1, number_2):
    result