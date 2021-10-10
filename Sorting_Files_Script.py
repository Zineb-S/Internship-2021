import os
import shutil
import hashlib
import time
from itertools import chain



def clean_folder(folder):
    while not os.path.isdir(folder):
        print("Folder not found :( ", end='\n')
        folder = input('Re-enter a valid folder path : ')
    else:
        print("Folder found !", end='\n')
        print('____________________________________________________')
        sort_files(folder)


def sort_files(folder):
    folder_hash(folder)
    ext_list = []
    li = os.listdir(folder)
    for i in li:
        file_name, extension = os.path.splitext(i)
        extension = extension[1:]
        ext_list.append(str(extension))
        if extension in ext_list:
            if os.path.exists(folder + '/' + extension):
                shutil.move(folder + '/' + i, folder + '/' + extension + '/' + i)
            else:
                os.makedirs(folder + '/' + extension)
                shutil.move(folder + '/' + i, folder + '/' + extension + '/' + i)

    print("Your files have been sorted")
    print("Current Folder -----> ", folder, " <-----")
    print('____________________________________________________')

    f_count(folder)
    after_sort(folder, li)
    delete_folder(folder)


def f_count(folder):
    no_ext = 0
    total_files = 0
    total_dir = 0
    for base, dirs, files in os.walk(folder):
        # print('Searching in : ', base)
        for directories in dirs:
            total_dir += 1
        for Files in files:
            total_files += 1
            file_name, extension = os.path.splitext(Files)
            if extension == "":
                no_ext += 1
    print("There is ", no_ext, "file(s) without extention(s)")
    print("Your total files", total_files)
    print("Your total folders", total_dir)
    print('____________________________________________________')


def after_sort(folder, li):
    print(len(li), "Folders recently created : ")
    li_ = os.listdir(folder)
    for i in li_:
        print("~ ", i, end="\n")
    print('____________________________________________________')


def delete_folder(folder):
    val = input("Do you want to delete any of these folders ? Y/N : ")
    val = str(val)[0].upper().strip()
    while val not in ['Y', 'N']:
        val = input("Input Yes (Y) or No (N) : ")
    if val == 'Y':
        to_remove = input("Which extension ?  ")
        folder2 = folder + '/' + str(to_remove)
        shutil.rmtree(folder2)
        print(to_remove, "is deleted !")
        print('____________________________________________________')
    else:
        print("Alright Alright bye ...")
        print('____________________________________________________')


def file_sha256(f_path):
    with open(f_path, "rb") as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(1024 * 1024):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def folder_hash(folder):
    info = {}
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isdir(path):
            folder_hash(path)
        else:
            # print("File: %s" % path)
            sha256 = file_sha256(path)
            # print("SHA256: %s\n" % sha256)
            b = os.path.getsize(path)
            # print(b)
            info[file] = (b, sha256)
    # printing initial_dictionary
    # print("initial_dictionary", str(info))
    # finding duplicate values
    # from dictionary using set
    rev_dict = {}
    for key, value in info.items():
        rev_dict.setdefault(value, set()).add(key)

    result = set(chain.from_iterable(
        values for key, values in rev_dict.items()
        if len(values) > 1))
    # print(result)
    # printing result
    if str(result) == "set()":
        print("There are no duplicates in ", folder)
    else:
        print("The duplicates in ", folder, " are : ", str(result))
        print('____________________________________________________')
        val = input("Do you want to delete any of these files ? Y/N : ")
        val = str(val)[0].upper().strip()
        while val not in ['Y', 'N']:
            val = input("Input Yes (Y) or No (N) : ")
        if val == 'Y':
            to_delete = str(input("Which one do you want to delete ? "))
            li = os.listdir(folder)
            for j in li:
                file_name, extension = os.path.splitext(j)
                if to_delete == j and j in result:
                    os.remove(folder + '/' + file_name + extension)
                    print(to_delete, " is deleted")
                    print('____________________________________________________')

def main():
    start_time = time.time()
    clean_folder(input('Enter folder path : '))
    print("___________________ END OF EXECUTION _____________________")
    print("--------------------- %.2f seconds -----------------------" % (time.time() - start_time))

start_time = time.time()
clean_folder(input('Enter folder path : '))
print("___________________ END OF EXECUTION _____________________")
print("--------------------- %.2f seconds -----------------------" % (time.time() - start_time))
if __name__ == "__main__":
    main()

# C:/Users/Admin/Downloads
