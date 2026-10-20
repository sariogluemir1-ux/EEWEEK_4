print("\n--- Part 7: Decimal to Binary Conversion ---")

decimal_num = int(input("Please enter a decimal number to convert to binary: "))
temp_num = decimal_num
remainders = ""

if decimal_num == 0:
    remainders = "0"
else:
    while temp_num > 0:
        remainder = temp_num % 2
        remainders = str(remainder) + remainders
        temp_num = temp_num // 2

print(f"Decimal {decimal_num} converted to binary is: {remainders}")