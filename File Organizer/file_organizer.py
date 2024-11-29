import os
import shutil

# Define the directory to organize
root_dir = input("Enter Path Directory: ")

# Define the file types and their corresponding subdirectories
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', 'csv'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'audio': ['.mp3', '.wav', '.ogg'],
    'archives': ['.zip', '.rar', '.7z', '.tar'],
    'others': []
}

def organize_files(root_dir):
    # Create subdirectories if they don't exist
    for subdirectory in file_types.keys():
        subdirectory_path = os.path.join(root_dir, subdirectory)
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)

    # Iterate through all files in the root directory
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(file_path)[1].lower()

        # Determine the subdirectory based on the file extension
        for subdirectory, extensions in file_types.items():
            if file_extension in extensions:
                subdirectory_path = os.path.join(root_dir, subdirectory)
                shutil.move(file_path, subdirectory_path)
                print(f"Moved '{filename}' to '{subdirectory}'")
                break
        else:
            # If the file type is not recognized, move it to 'others'
            subdirectory_path = os.path.join(root_dir, 'others')
            shutil.move(file_path, subdirectory_path)
            print(f"Moved '{filename}' to 'others'")

if __name__ == "__main__":
    organize_files(root_dir)