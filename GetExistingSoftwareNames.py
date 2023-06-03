import subprocess

# Specify the directory path
directory = r'E:\Softwares\Full Software'

# Run the command and capture the output
command = f'dir /AD /B /S "{directory}"'
output = subprocess.check_output(command, shell=True, encoding='utf-8')

# Process the output to extract the result after the third "\"
lines = output.split('\n')
result = [line.split('\\', 3)[-1] for line in lines if line]

# Print the modified output
for item in result:
    print(item)
