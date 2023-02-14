import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Path to a file where the download folder path will be saved
CONFIG_FILE = "config.txt"

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Check if the config file exists
if os.path.exists(CONFIG_FILE):
    # If it exists, read the download folder path from the file
    with open(CONFIG_FILE, "r") as f:
        download_folder = f.read().strip()
else:
    # If it doesn't exist, ask the user to select the download folder
    download_folder = filedialog.askdirectory(title="Select the download folder")
    # Ask the user if they want to save the download folder path for future use
    save_path = input("Do you want to save the download folder path? (y/n) ")
    if save_path.lower() == "y":
        # If yes, save the path to the config file
        with open(CONFIG_FILE, "w") as f:
            f.write(download_folder)

# List of specific file types that you want to move to different folders
specific_file_types = ['.exe', '.mp3', '.mp4', '.png', '.jpg', '.pdf', '.rar', '.zip', '.txt']

# Get list of files in the download folder
files = os.listdir(download_folder)

# Move specific file types to their own folders
for file in files:
    file_extension = os.path.splitext(file)[1]
    if os.path.isfile(os.path.join(download_folder, file)):
        if file_extension in specific_file_types:
            # Check if folder for file extension already exists
            if os.path.exists(download_folder + "\\" + file_extension):
                shutil.move(download_folder + "\\" + file, download_folder + "\\" + file_extension + "\\" + file)
            else:
                os.mkdir(download_folder + "\\" + file_extension)
                shutil.move(download_folder + "\\" + file, download_folder + "\\" + file_extension + "\\" + file)
        else:
            if not os.path.exists(download_folder + "\\others"):
                os.mkdir(download_folder + "\\others")
            shutil.move(download_folder + "\\" + file, download_folder + "\\others\\" + file)
