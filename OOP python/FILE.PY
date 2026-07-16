from pathlib import Path
import os
path = Path("D:/DSA")
file_count = 0
dir_count = 0
for item in path.rglob("*"):
    if item.is_file():
        file_count+=1
    elif item.is_dir():
        dir_count+=1
print("files:", file_count)
print("directory", dir_count)

while True:
    print("-------menu--------")
    print("1.create file")
    print("2.create directory")
    print("3.exit")
    choice = int(input("enter your choice:"))


    if choice == 1:
        e = input("enter your file path here:")
        if os.path.exists(e):
            print("file already exists")
        else:
            with open(e, 'w') as f:
                f.write("")
            print(f"file created ")
    
    elif choice ==2 :
        path1 = input("enetr your directory name:")
        if os.path.exists(path1):
            print("directory existed")
        else:
            os.makedir(path1)
            print("directory created")

    elif choice ==3:
        print("exiting ")
        break
    else:
        print("invalid choice")


