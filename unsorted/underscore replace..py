import os

# Set the directory path
dir_path = './'

# Loop through all files in the directory
for file_name in os.listdir(dir_path):
    # Check if the file is a text file
    if file_name.endswith('.txt'):
        # Read the contents of the file
        with open(os.path.join(dir_path, file_name), 'r') as f:
            contents = f.read()
        # Replace underscores in the contents
        contents = contents.replace('_', ' ')
        # Write the modified contents back to the file
        with open(os.path.join(dir_path, file_name), 'w') as f:
            f.write(contents)