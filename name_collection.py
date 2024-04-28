# Open the file and read lines into a list
file_path = 'C:\\Users\\Hamza Yasin\\Downloads\\what\\groups.txt'  # Replace 'your_file.txt' with your actual file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove newline characters from each string
lines = [line.strip() for line in lines]

# lines is now a list of strings from the file
print(lines)
