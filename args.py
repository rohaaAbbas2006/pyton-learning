# def printArgs(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", args, kwargs)
#         result = func(*args, **kwargs)
#         print("Result:", result)
#         return result
#     return wrapper

# @printArgs
# def multiplication(num1, num2, method):
#     if method == "*":
#         return num1 * num2
#     elif method == "+":
#         return num1 + num2
#     elif method == "-":
#         return num1 - num2
#     elif method == "/":
#         return num1 / num2
#     else:
#         return "Invalid method"

# print(multiplication(10, 5, "+"))


import argparse

# Create the parser
parser = argparse.ArgumentParser()
print(type(parser))

# Add arguments
parser.add_argument('--name', type=str, required=True, help='Your name')

# Parse arguments
args = parser.parse_args()

# Access the value
print(f"Hello, {args.name}!")
