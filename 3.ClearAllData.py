import os

def delete_files_and_folders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

# Specify the folder paths
folder_paths = ["Result", "Final_Result"]

# Delete files and folders in each specified folder
for folder_path in folder_paths:
    delete_files_and_folders(folder_path)
