from local_lib.path import Path

def _use_path():
    folder_name = "ex01_folder"
    file_name = "ex01_file_name.txt"

    folder = Path(folder_name)
    file_path = folder / file_name  # Way to create the path : "ex01_folder/ex01_file_name.txt" 

    folder.mkdir_p()
    file_path.write_text('This is a text example wrote in the file!')
    print(file_path.read_text())

if __name__ == "__main__":
    try:
        _use_path()
    except Exception as e:
        print(e)

