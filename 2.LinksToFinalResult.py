import os

folder_path = "Result"  # Path to the main folder
output_folder = "Final_Result"  # Name of the output folder

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all subfolders within the main folder
subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

# Iterate over each subfolder
for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    
    # Get a list of all text files within the subfolder
    file_list = [file for file in os.listdir(subfolder_path) if file.endswith(".txt")]
    
    # Sort the file list
    file_list.sort()
    
    # Combine the contents of all text files in the subfolder
    combined_content = ""
    for filename in file_list:
        file_path = os.path.join(subfolder_path, filename)
        with open(file_path, "r") as file:
            combined_content += file.read()
    
    # Save the combined contents to the output file
    output_file = os.path.join(output_folder, "Final_Result_" + subfolder + ".txt")
    with open(output_file, "w") as outfile:
        outfile.write(combined_content)

print("Files combined successfully.")
