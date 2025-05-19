# This is being used for running the bash script (1)
import subprocess




# This part creates a bash script on the machine.

# with - allows you to manage resources like files
# open - using the x option it either creates a file with the name given or fails if it already exists
# as file - is used so that files are opened and closed properly

with open('conspic-u-us.sh', 'x') as file:

# At this point if 'conspic-u-us.sh' already exists the rest doesn't run since it fails.
# This means we can run this script as a task and won't need to worry about it creating duplicate files.

    file.write("""#!/bin/bash

# Set the filename with timestamp to avoid overwriting
filename="document_$(date +%Y%m%d_%M%S).txt"

# Create the file
touch "$filename"

# Optional: Add some default content
echo "This is a new document created on $(date)." > "$filename"

# Confirm creation
                   
echo "Document '$filename' created successfully.""")

# This is telling the program to run the script that we just barely created.
# It also makes sure that it is running and when not which error it is.

result = subprocess.run(['./conspic-u-us.sh'], capture_output=True, text=True, shell=True)

# Check the exit code
if result.returncode == 0:
    print("Script executed successfully.")
    print("Output:", result.stdout)
else:
    print("Script failed with error code:", result.returncode)
    print("Error:", result.stderr)