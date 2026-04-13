import os
import datetime

def list_contents(path):
    print(f"\n Contents of:{path}")
    try:
        items=os.listdir(path)
        for item in items:
            full_path=os.path.join(path,item)
            print("file" if os.path.isfile(full_path) else 'folder',item)
    except FileNotFoundError:
        print("path not found")

def create_folder(path,folder_name):
    full_path=os.path.join(path,folder_name)
    try:
        os.mkdir(full_path)
        print(f"folder created:{folder_name}")
    except FileExistsError:
        print('folder already exists.')

def delete_item(path,name):
    full_path=os.path.join(path,name)
    if os.path.isdir(full_path):
        os.rmdir(full_path)
        print(f"folder deleted:{name}")
    elif os.path.isfile(full_path):
        os.remove(full_path)
        print(f"file deleted:{name}")
    else:
        print("file/folder not found")

def show_file_info(path,name):
    full_path=os.path.join(path,name)
    if os.path.exists(full_path):
        created=datetime.datetime.fromtimestamp(os.path.getctime(full_path))
        modified=datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
        print(f"\ninfo for:{name}")
        print("created:",created)
        print("modified:",modified)
    else:
        print("file not found")

folder_path = input("Enter folder path")

while True:
    print("\n mini file manager")
    print("1. List contents")
    print("2. Create folder")
    print("3. Delete file/folder")
    print("4. File info")
    print("5. Exit")

    choice=input("Enter choice:(1-5):")

    if choice == '1':
        list_contents(folder_path)
    elif choice == '2':
        name=input("Enter folder name to create:")
        create_folder(folder_path,name)
    elif choice == '3':
        name=input("Enter file/folder name to delete:")
        delete_item(folder_path,name)
    elif choice == '4':
        name=input("Enter file name:")
        show_file_info(folder_path,name)
    elif choice == '5':
        print("Exiting file manager.")
        break
    else:
        print("Invalid choice..")







