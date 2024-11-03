try:
    number = int(input("enter a number: "))
    print("the number entered is", number)
except ValueError as ex:
    print("Exception:", ex)
try:
    num1,num2 = eval(input("enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("Comma is missing. Enter number seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")
