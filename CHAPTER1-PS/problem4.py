import os

# Specify the directory path
directory_path = "../"  # Current directory, or replace with a specific path like "C:/Users/Documents"

# Get the list of contents in the directory
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)