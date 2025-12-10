sum=0
try:
    with open(r"C:\Users\bonssa.teizazu\OneDrive - General Dynamics Mission Systems\Desktop\Day3.txt", "r") as file:
        for line in file:
            # line includes the newline character (\n) at the end
            # Use .strip() to remove leading/trailing whitespace, including newline
            joltageRating = line.strip()
            print(joltageRating)
            
            i=0
            left=1
            
            for digit in joltageRating[:-1]:
                int_digit = int(digit)
                
                if (int_digit>left):
                    left = int_digit
                    maxIndex = i
                i += 1
            
            i=0    
            right = 1
            for digit in joltageRating[maxIndex+1:]:
                int_digit = int(digit)
                if (int_digit>right):
                    right = int_digit
                i += 1
            MaxJoltage = int(str(left)+str(right))
            print(f"\tMax Joltage: {MaxJoltage}")
            sum += MaxJoltage

    print(f"Sum: {sum}")  

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
