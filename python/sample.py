def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(farewell("World"))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 10 by 2:", divide(10,