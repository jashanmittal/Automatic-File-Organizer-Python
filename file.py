import os
import shutil
import time

while True:

    if (not os.path.exists("PyFiles")):
        os.mkdir("PyFiles")

    if (not os.path.exists("PyFiles/Python_Files")):
        os.mkdir("PyFiles/Python_Files")

    if (not os.path.exists("PyFiles/Photo")):
        os.mkdir("PyFiles/Photo")

    if (not os.path.exists("PyFiles/Text")):
        os.mkdir("PyFiles/Text")

    files = os.listdir("PyFiles")
    
    for file in files:

        if not os.path.isfile(f"PyFiles/{file}"):
            continue

        extension = os.path.splitext(file)[1]

        if extension == ".py":
            shutil.move(f"PyFiles/{file}", f"PyFiles/Python_Files/{file}")
        elif extension in [".jpg", ".png", ".jpeg", ".bmp"]:
            shutil.move(f"PyFiles/{file}", f"PyFiles/Photo/{file}")
        elif extension == ".txt":
            shutil.move(f"PyFiles/{file}", f"PyFiles/Text/{file}")

        elif extension in [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"]:
            if (not os.path.exists("PyFiles/Video")):
                os.mkdir("PyFiles/Video")
            shutil.move(f"PyFiles/{file}", f"PyFiles/Video/{file}")

        elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"]:
            if (not os.path.exists("PyFiles/Archives")):
                os.mkdir("PyFiles/Archives")
            shutil.move(f"PyFiles/{file}", f"PyFiles/Archives/{file}")

        elif extension in [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".odt"]:
            if (not os.path.exists("PyFiles/Documents")):
                os.mkdir("PyFiles/Documents")
            shutil.move(f"PyFiles/{file}", f"PyFiles/Documents/{file}")

        else:
            if (not os.path.exists("PyFiles/Other")):
                os.mkdir("PyFiles/Other")
            shutil.move(f"PyFiles/{file}", f"PyFiles/Other/{file}")

    print("Successfully Arranged")
    time.sleep(10)
