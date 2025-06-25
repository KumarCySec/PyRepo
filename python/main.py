def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 from 10:", subtract(10, 5))