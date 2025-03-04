import os
import shutil

# Define file categories and their respective extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".FLAC"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}#above given the all categories of file.

def organize_files(directory):
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Move files into respective category folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break #using break
            
            # Move to 'Others' if no category matches
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file))
    
    print("File organized successfully!")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
