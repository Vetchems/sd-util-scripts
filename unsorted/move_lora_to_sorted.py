import os
import shutil

def search_and_move_files(folder_path):
    # Create the 'sorted' folder if it doesn't exist
    sorted_folder = os.path.join(folder_path, 'sorted')
    if not os.path.exists(sorted_folder):
        os.mkdir(sorted_folder)

    # Recursively search for .pt and .safetensors files and move them to the 'sorted' folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pt') or file.endswith('.safetensors'):
                file_path = os.path.join(root, file)
                destination_file_path = os.path.join(sorted_folder, file)
                if not os.path.exists(destination_file_path):
                    shutil.move(file_path, sorted_folder)
                    print(f"Moved {file_path} to {sorted_folder}.")
                else:
                    print(f"Skipping {file_path} as it already exists in {sorted_folder}.")
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) > 0:
                    destination_file_path = os.path.join(sorted_folder, file)
                    if not os.path.exists(destination_file_path):
                        shutil.move(file_path, sorted_folder)
                        print(f"Moved {file_path} to {sorted_folder}.")
                    else:
                        print(f"Skipping {file_path} as it already exists in {sorted_folder}.")
        # Delete subfolders (except 'sorted' folder)
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if dir_path != sorted_folder:
                shutil.rmtree(dir_path)
                print(f"Deleted {dir_path}.")
# Specify the folder path where the search should start
folder_path = './'

# Call the function to search and move files
search_and_move_files(folder_path)
