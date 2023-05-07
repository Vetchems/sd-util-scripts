import datetime

# Get the current date and time to include in the output filename
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d_%H-%M-%S")

# Input filenames
file1 = 'list1.txt'
file2 = 'list2.txt'

# Output filename
output_file = f'prompts_{date_string}.txt'

# Read the contents of the input files into sets
with open(file1, 'r') as f1, open(file2, 'r') as f2:
    set1 = set([line.strip() for line in f1])
    set2 = set([line.strip() for line in f2])

# Combine the sets and write the unique values to the output file
with open(output_file, 'w') as f:
    unique_values = set1.union(set2)
    for value in unique_values:
        f.write(value + '\n')

print(f'Successfully merged {file1} and {file2} into {output_file}.')
