import os

def search_and_write_filenames(folder_path, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Recursively search for .pt and .safetensors files and write filenames to the output file
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.pt') or file.endswith('.safetensors'):
                    file_name = os.path.splitext(file)[0]  # Get the filename without extension
                    outfile.write(f'<lyco:{file_name}:{weight}>\n')

# Specify the folder path where the search should start
folder_path = './'

weight = 0.9

# Specify the output file path
output_file = f'./lyco_w{weight}.txt'



# Call the function to search and write filenames to the output file
search_and_write_filenames(folder_path, output_file)
