import os
import shutil

path = "test.txt"

try:
    os.remove(path) # delete a file
    # os.rmdir(path) # remove an empty directory
    # shutil.rmtree(path) # remove a nonempty directory
except FileNotFoundError:
    print(f"File {path} was not found")
else:
    print(f"{path} was deleted")

# does not remote empty folders
# for deleting an empty folder use rmdir instead of remove
# for removing directory which is not empty use shutil.rmtree(path) and import shutil