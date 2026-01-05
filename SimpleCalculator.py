import sys

def main():
    number1, number2 = userinput()
    addition(number1, number2)
    subtraction(number1, number2)  
    multiplication(number1, number2)
    division(number1, number2)
    
def userinput():
    while True:
        try:
            number1 = float(input("Please input the first number: "))
            number2 = float(input("Please input the seconde number: "))
            return number1,number2
        except ValueError:
            continue

def addition(number1, number2):
    print(f"{number1} + {number2} = {number1+number2}") 
    
def subtraction(number1, number2):
    print(f"{number1} - {number2} = {number1-number2}") 

def multiplication(number1, number2):
    print(f"{number1} * {number2} = {number1*number2}") 

def division(number1, number2):
    try:
        result = number1/number2
        print(f"{number1} / {number2} = {result}")
    except ZeroDivisionError:
        sys.exit("division by zero error!")

if __name__ == "__main__":
    main()
