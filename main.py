def binary_to_decimal(binary):
    try:
        # Convert binary string to decimal
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        return "Invalid binary input. Please enter only 0's and 1's."

# Example usage
binary_code = input("Enter the binary code: ")
decimal_value = binary_to_decimal(binary_code)
print(f"The decimal equivalent of {binary_code} is {decimal_value}.")
