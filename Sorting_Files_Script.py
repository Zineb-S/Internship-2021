import os
#  Permet l'utilisation des fonctionnalités dépendantes du système d'exploitation
# ( Dans ce code --> Manipuler les chemins des fichiers et leurs extensions)

import os
import shutil
#  Manipulation de fichiers et de répertoires de haut niveau
# ( Dans ce code --> Déplacer les fichiers )

dirName = input('Enter folder path : ')
# Saisie du chemin du fichier qu'on veut filtrer


li = os.listdir(dirName)
# Renvoie une liste contenant les noms des entrées (fichiers) dans le répertoire donné par chemin
# exemple : ['Convention de stage.xlsx', 'python-3.9.6-amd64.exe','Sujet_de_stage.pdf']
def clean_folder(folder):
    while not os.path.isdir(folder):
        print("Folder not found :( ",end='\n')
        folder = input('Re-enter a valid folder path : ')
    else:
        print("Folder found !",end='\n')
        print('____________________________________________________')
        sort_files(folder)

def sort_files(folder):
    find_doubles(folder)
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
    print("Current Folder -----> " ,folder," <-----")
    print('____________________________________________________')

for i in li:
    # Parcourir la liste contenant les  noms des entrées
    f_count(folder)
    after_sort(folder,li)
    delete_folder(folder)

    fileName, extension = os.path.splitext(i)
    # Séparation des extensions des noms des fichiers en une paire (racine, ext)
    # racine + ext == chemin du fichier
    # ext soit vide ou commence par un point et contienne au plus un point.
def f_count(folder):
    no_ext = 0
    totalFiles = 0
    totalDir = 0
    for base, dirs, files in os.walk(folder):
        #print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
            file_name, extension = os.path.splitext(Files)
            if extension == "":
                no_ext+=1
    print("There is ", no_ext, "file(s) without extention(s)")
    print("Your total files",totalFiles)
    print("Your total folders",totalDir)
    print('____________________________________________________')

    extension = extension[1:] # Enlever le (.)

    if extension == "":  # On passe au cas d'abscence d'extension
        continue

    if os.path.exists(dirName + '/' + extension):                               # True si chemin fait référence à un chemin existant ,False si non
        shutil.move(dirName + '/' + i, dirName + '/' + extension + '/' + i)     # Si le chemin est existant on y déplace le fichier
                   # shutil.move(src, dst, copy_function=copy2)
def after_sort(folder,li):
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
    else:
        os.makedirs(dirName + '/' + extension)                                  # Si non on crée un répertoire
        shutil.move(dirName + '/' + i, dirName + '/' + extension + '/' + i)     # On y déplace le fichier
        print("Alright Alright bye ...")


def find_doubles(folder):
    print("hi")


clean_folder(input('Enter folder path : '))
# C:/Users/Admin/Downloads
