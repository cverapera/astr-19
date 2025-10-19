# Define the function f(x)
def f(x):
    return x**3 + 8

# Main part of the program
def main():
    x = 9
    result = f(x)
    print("f(x) =", result)

    if result > 27:
        print("YAY!")

# Call the main function
main()