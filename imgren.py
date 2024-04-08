import os
import uuid
from datetime import datetime

# Path to the folder containing files
folder_path = '/Users/gaobo/Downloads/dsync/common/imv/stgimg/'

# Get list of files in the folder
files = os.listdir(folder_path)

# Sort files by creation time
files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

# Get current date in YYMMDD format
current_date_suffix = datetime.now().strftime("%y%m%d")

# Specify the starting number
start_number = 0  # Adjust this as needed

# Rename and number files sequentially with leading zeros for five digits
for i, filename in enumerate(files):
    # Get file extension and convert it to lowercase
    filename_without_extension, extension = os.path.splitext(filename)
    extension = extension.lower()
    
    # Generate a GUID and format it without hyphens
    guid_suffix = str(uuid.uuid4()).replace('-', '')
    
    # New filename with leading zeros for five digits, GUID suffix, and date suffix
    new_filename = f"{start_number + i:05d}-{current_date_suffix}-{guid_suffix}{extension}"
    
    # Old and new file paths
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    
    # Rename file
    #os.rename(old_path, new_path)

    print(f"Renamed: {filename} to {new_filename}")