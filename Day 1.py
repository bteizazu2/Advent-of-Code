num = 50
password=0

try:
    with open(r"PATH TO PUZZLE INPUT HERE", "r") as file:
        for line in file:
            # line includes the newline character (\n) at the end
            # Use .strip() to remove leading/trailing whitespace, including newline
            step = line.strip()
            if step[0] == "L":
                num = (num-int(step[1:])) % 100
            else:
                num = (num+int(step[1:])) % 100
            if num ==0:
                password += 1
            print(num, password)
            
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
