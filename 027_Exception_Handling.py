
try:
    numerator = int(input("Num1: "))
    denominator = int(input("Num2: "))
    result = numerator / denominator    
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by Zero")
except ValueError as e:
    print(e)
    print("enter only numbers please")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")