# try:
with open("input.txt", "r", encoding='utf8') as infile:
    line = infile.readline().split()
    num1, num2 = line

    a = int(num1)
    b = int(num2)
    res = a + b

with open("output.txt", "w", encoding='utf8') as outfile:
    outfile.write(str(res))

#     print("Successfully read input, calculated sum, and wrote to output file.")

# except FileNotFoundError:
#     print("Error: One or both of the input/output files were not found.")
# except ValueError:
#     print("Error: Invalid input in the file. Please ensure two numbers separated by a space are present.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
