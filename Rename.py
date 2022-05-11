import os

path = "Yours dir path , remenber useing / , don't use \ , otherwise that will be a wrong"
files = os.listdir(path)
print(f"Before Renaming: {files}")
for i in range(len(files)):
   os.rename(path+files[i], f"{path}filename{i+1}.PNG")
print(f"After Renaming: {os.listdir(path)}")
