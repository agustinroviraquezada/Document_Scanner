import os
from google.colab import drive

def mount_drive():
    """
    Mounts Google Drive to the Colab environment.
    """
    print("Mounting Google Drive...")
    drive.mount('/content/drive')
    print("Google Drive mounted successfully!")

def choose_working_directory():
    """
    Prompts the user for a directory path within Google Drive to set as the working directory.
    """
    print("Please enter the path of the directory within your Google Drive that you want to use as your working directory.")
    print("Example: '/content/drive/My Drive/Colab Projects/Project Name'")
    working_dir = input("Enter your working directory path: ")

    # Check if the directory exists
    if not os.path.exists(working_dir):
        print(f"The directory '{working_dir}' does not exist.")
        return None

    # Set the working directory
    os.chdir(working_dir)
    print(f"Working directory changed to: {working_dir}")
    return working_dir

if __name__ == "__main__":
    mount_drive()
    working_dir = choose_working_directory()

    if working_dir:
        print(f"Setup completed. Your working directory is: {working_dir}")
    else:
        print("Setup failed. Please check the directory path and try again.")
