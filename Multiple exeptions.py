try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the first number: "))
    result = num1 / num2
    print("Result is ",result)
except ZeroDivisionError:
    print("Division by zero is error.")
except ValueError:
    print("Please enter a whole number.")
except:
    print("Wrong input.")
else:
    print("No exeptions.")
finally:
    print("This will execute no matter what")