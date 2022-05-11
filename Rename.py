import os

path = "/tensorflow1/models/research/object_detection/images/train/"
files = os.listdir(path)
print(f"Before Renaming: {files}")
for i in range(len(files)):
   os.rename(path+files[i], f"{path}00{i+1}.PNG")
print(f"After Renaming: {os.listdir(path)}")
