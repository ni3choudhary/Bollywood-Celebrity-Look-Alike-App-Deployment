# Python 3 code to rename multiple files in a directory or folder

# importing os module
import os

folder = "data"
actors = os.listdir(folder) 

# Function to rename multiple folders
def rename_folder():
    for actor in actors:
        for i in range(len(actor)):
            if actor[i] == ' ':
                dst = actor.replace(' ', '_')
                src =f"{folder}/{actor}" # foldername/filename, if .py file is outside folder
                dst =f"{folder}/{dst}"
                os.rename(src,dst)
            else:
                print("The Folder Already Exists with Proper Format")
    

# Function to rename multiple files
def rename_files():
    actors = os.listdir(folder)
    for actor in actors:
        for count, filename in enumerate(os.listdir(os.path.join(folder,actor))):
            dst = f"{actor}_{str(count)}.jpg"
            src =f"{folder}/{actor}/{filename}" # foldername/filename, if .py file is outside folder
            dst =f"{folder}/{actor}/{dst}"
            # rename() function will rename all the files
            if os.path.isfile(dst):
                print("The File Already Exists")
            else:
                # Rename the file
                os.rename(src, dst)
        
        

# main function for calling other functions
def main():
    rename_folder()
    rename_files()

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
