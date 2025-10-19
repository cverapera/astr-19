import math
import numpy as np

def main():
    # Create 1000 evenly spaced values between 0 and 2
    x_values = np.linspace(0, 2, 1000)

    # Print the header
    print("x\t\tsin(x)")
    print("-" * 25)

    # Loop through x values and print sin(x)
    for x in x_values:
        print(f"{x:.6f}\t{math.sin(x):.6f}")

# Call the main function
if __name__ == "__main__":
    main()