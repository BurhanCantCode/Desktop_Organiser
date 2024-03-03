import os
import shutil

def organize_desktop():
    # Define paths to desktop and folders
    desktop_path = os.path.expanduser("~/Desktop")
    pdf_folder = os.path.join(desktop_path, "pdfs")
    image_folder = os.path.join(desktop_path, "images")
    games_folder = os.path.join(desktop_path, "games")
    excel_folder = os.path.join(desktop_path, "excel")
    word_folder = os.path.join(desktop_path, "word")
    notepad_folder = os.path.join(desktop_path, "notepad")
    OOP_folder = os.path.join(desktop_path, "OOP")
    C_folder= os.path.join(desktop_path, "C")


    # Create folders if they don't exist
    for folder in [pdf_folder, image_folder, games_folder, excel_folder, word_folder, notepad_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Get list of files on desktop
    files_on_desktop = os.listdir(desktop_path)

    # Organize files
    for file_name in files_on_desktop:
        file_path = os.path.join(desktop_path, file_name)

        if file_name.lower().endswith(".pdf"):
            shutil.move(file_path, pdf_folder)
            print(f"Moved {file_name} to PDFs folder.")
        elif file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            shutil.move(file_path, image_folder)
            print(f"Moved {file_name} to Images folder.")
        elif file_name.lower().endswith((".exe", ".msi",".lnk")):
            shutil.move(file_path, games_folder)
            print(f"Moved {file_name} to Games folder.")
        # Add more conditions for other file types as needed
        #adding for excel word and notepad txt files making seperate folders for each
        elif file_name.lower().endswith((".xlsx", ".xls")):
            shutil.move(file_path, excel_folder)
            print(f"Moved {file_name} to Excel folder.")
        elif file_name.lower().endswith((".doc", ".docx")):
            shutil.move(file_path, word_folder)
            print(f"Moved {file_name} to Word folder.")
        elif file_name.lower().endswith(".txt"):
            shutil.move(file_path, notepad_folder)
            print(f"Moved {file_name} to Notepad folder.")
        elif file_name.lower().endswith((".cpp")):
            shutil.move(file_path, OOP_folder)
            print(f"Moved {file_name} to OOP folder.")
        elif file_name.lower().endswith((".c")):
            shutil.move(file_path, C_folder)
            print(f"Moved {file_name} to C folder.")
            
        

    print("Desktop organized successfully.")

if __name__ == "__main__":
    organize_desktop()


