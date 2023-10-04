try:
    # Code block where an exception might occur
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

    print("The result is:", result)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("An error occurred:", str(e))