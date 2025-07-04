import os
import shutil
import time
import sys

# ==============================
# 📁 Windows File Organizer
# ------------------------------
# Organizes your Downloads folder into subfolders based on file types:
# zip, image, pdf, exe, sound, video, OS images (ISO), and random.
# made by TR4IS on Github <3
# ==============================

# Get the current user's Downloads folder
user = os.getlogin()
download_path = f"C:/Users/{user}/Downloads"

# Define the folder categories and their associated file extensions
file_types = {
    'zip': ['.zip', '.rar'],
    'image': ['.png', '.jpg', '.gif', '.jpeg', '.psd'],
    'pdf': ['.pdf'],
    'exe': ['.exe', '.msi'],
    'sound': ['.mp3', '.wav', '.ogg', '.flac', '.m4a'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'os': ['.iso', '.img'],
    'random': []  # Everything else goes here
}

print("Organize all files in Download folder\n")
choice  = input("continue ? (Y/n)").lower()
if choice == "n":
    exit()
elif choice == "y":
    # Create folders if they don't already exist
    for folder in file_types.keys():
        folder_path = os.path.join(download_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"[+] Created folder: {folder_path}")

    # List everything in Downloads
    items = os.listdir(download_path)

    # Skip folders used for sorting to avoid moving them
    sort_folders = set(file_types.keys())

    # Go through each item in Downloads
    for item in items:
        item_path = os.path.join(download_path, item)

        # Skip the folders created for sorting
        if item.lower() in sort_folders:
            continue

        # Get the file extension
        _, ext = os.path.splitext(item.lower())

        # Try to match the file to a known category
        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                dest_path = os.path.join(download_path, folder, item)
                shutil.move(item_path, dest_path)
                print(f"[→] Moved: {item} → {folder}/")
                moved = True
                break

        # If no match, move to 'random'
        if not moved:
            dest_path = os.path.join(download_path, 'random', item)
            shutil.move(item_path, dest_path)
            print(f"[→] Moved: {item} → random/")

    #def animate_dots(message="🟥 Shutting down", dot_count=3, repeat=1, delay=0.5):
    #    for _ in range(repeat):
    #        for i in range(dot_count + 1):
    #            dots = '.' * i
    #            sys.stdout.write('\r' + message + dots + ' ' * (dot_count - i))  # Clear extra dots
    #            sys.stdout.flush()
    #            time.sleep(delay)
    #    print('\r' + message + '...' + ' ' * dot_count)  # Final state

    print("\n✅ Done organizing your Downloads folder!")
    input("💢 Press enter to exit")
    #animate_dots()
