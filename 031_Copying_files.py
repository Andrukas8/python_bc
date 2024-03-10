import shutil

# copyfile() - copies the contents of a file
# copy() - copyfile() + permission mode + destination can be a directory
# copy2() - copy() + metadata

shutil.copyfile("test.txt", "copy.txt")
