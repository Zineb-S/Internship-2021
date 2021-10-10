import os
#  Permet l'utilisation des fonctionnalités dépendantes du système d'exploitation
# ( Dans ce code --> Manipuler les chemins des fichiers et leurs extensions)

import shutil
#  Manipulation de fichiers et de répertoires de haut niveau
# ( Dans ce code --> Déplacer les fichiers )

import hashlib
# Implémente une interface commune à de nombreux algorithmes de hachage sécurisés
# (Dans ce code --> utilisez sha256() pour créer un objet de hachage SHA-256 / Hachage des fichiers)

import time
# Calculer le temps d'exécution

from itertools import chain
# Créer une chaine à partir d'un itérable

class Folder:

    def __init__(self, folder):  # Initialisation d'un objet (dossier) qu'on va trier
        self.folder = folder

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
    def clean_folder(self, folder):  # Chercher le dossier d'après le chemin saisi

        while not os.path.isdir(self.folder):
            print("Folder not found :( ", end='\n')
            self.folder = input(
                'Re-enter a valid folder path : ')  # Si on arrive pas à le trouver --> ressaisir le chemin
        else:
            print("Folder found !", end='\n')  # Si non on passe au tri du dossier
            print('____________________________________________________')
            self.sort_files(self.folder)

    def sort_files(self, folder):

        ext_list = []

        self.folder_hash(self.folder)    # Voir la fonction folder_hash
        li = os.listdir(self.folder)
        # Renvoie une liste contenant les noms des entrées (fichiers) dans le répertoire donné par chemin
        # exemple : ['Convention de stage.xlsx', 'python-3.9.6-amd64.exe','Sujet_de_stage.pdf']

        for i in li:
            # Parcourir la liste contenant les  noms des entrées
            file_name, extension = os.path.splitext(i)
            # Séparation des extensions des noms des fichiers en une paire (racine, ext)
            # racine + ext == chemin du fichier
            # ext soit vide ou commence par un point et contienne au plus un point.

            extension = extension[1:]
            # Enlever le (.)
            ext_list.append(str(extension)) # liste qui contient les extensions
            if extension in ext_list:
                if os.path.exists(self.folder + '/' + extension):                                  # True si chemin fait référence à un chemin existant ,False si non
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)    # Si le chemin est existant on y déplace le fichier
                    # shutil.move(src, dst, copy_function=copy2)
                else:
                    os.makedirs(self.folder + '/' + extension)                                     # Si non on crée un répertoire
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)    # On y déplace le fichier

        print("Your files have been sorted")
        print("Current Folder -----> ", self.folder, " <-----")
        print('____________________________________________________')
    else:
        print("Alright Alright bye ...")

        self.f_count(self.folder)          # Compter le nb de fichier / dossier
        self.after_sort(self.folder, li)   # Lister le contenu du dossier après le tri
        self.delete_folder(self.folder)    # Suppression des dossiers par extension

    def f_count(self, folder):

        no_ext = 0
        total_files = 0
        total_dir = 0

        for base, dirs, files in os.walk(self.folder): # Parcourir le dossier parent
            # print('Searching in : ', base)
            for directories in dirs:
                total_dir += 1           # Compter le nb de dossier
            for Files in files:
                total_files += 1         # Compter le nb de fichier
                file_name, extension = os.path.splitext(Files)
                if extension == "":      # Trouver des fichiers sans extensions
                    no_ext += 1

        print("There is ", no_ext, "file(s) without extention(s)")
        print("Your total files", total_files)
        print("Your total folders", total_dir)
        print('____________________________________________________')

    def after_sort(self, folder, li):

def file_sha256(f_path):
    with open(f_path, "rb") as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(1024 * 1024):
            file_hash.update(chunk)
    return file_hash.hexdigest()
        print(len(li), "Folders recently created : ")
        li_ = os.listdir(self.folder)
        # Renvoie une liste contenant les noms des entrées (fichiers) dans le répertoire donné par chemin
        # Voir les dossiers récemment créés après le tri
        for i in li_:
            print("~ ", i, end="\n")
        print('____________________________________________________')

    def delete_folder(self, folder):

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
        val = input("Do you want to delete any of these folders ? Y/N : ")
        val = str(val)[0].upper().strip()
        while val not in ['Y', 'N']:
                                                                        # Voir si l'utilisateur veut supprimer
        while val not in ['Y', 'N']:                                    # un dossier en fonction des extensions

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

if __name__ == "__main__":
    main()

# C:/Users/Admin/Downloads
            to_remove = input("Which extension ?  ")                    # choisir une extension
            self.folder2 = self.folder + '/' + str(to_remove)
            shutil.rmtree(self.folder2 )                                # suppression du dossier
            print(to_remove, "is deleted !")
            print('____________________________________________________')
        else:
            print("Alright Alright bye ...")
            print('____________________________________________________')

    def file_sha256(self, f_path):   # hachage des fichiers

        with open(f_path, "rb") as f:            # ouvrir le fichier
            file_hash = hashlib.sha256()         # utilisation de l'algorithme sha256 pour l'hachage du fichier
            while chunk := f.read(1024 * 1024):  # Lire un nombre d'octet du fichier
                file_hash.update(chunk)          
        return file_hash.hexdigest()             # Renvoie une valeur hexadécimale plus facile à manipuler 

    def folder_hash(self, folder):
        info = {}
        for file in os.listdir(self.folder):  #Parcourir les fichiers dans le dossier parent
            path = os.path.join(self.folder, file) # Jointure du chemin du dossier avec le fichier
            if os.path.isdir(path):    # si le chemin existe
                self.folder_hash(path)  # hachage en utilisant le chemin
            else:
                # print("File: %s" % path)         # Si non hashage directe du fichier
                sha256 = self.file_sha256(path)
                # print("SHA256: %s\n" % sha256)

                b = os.path.getsize(path)         # calculer la taille du fichier
                # print(b)

                info[file] = (b, sha256)         # insertion d'un couple clé valeur avec le nom de fichier comme clé et
                                                  # un tuple ( taille du fichier , hash code du fichier ) comme valeur

        # printing initial_dictionary
        # print("initial_dictionary", str(info))
        # finding duplicate values
        # from dictionary using set
        rev_dict = {}
        for key, value in info.items():
            rev_dict.setdefault(value, set()).add(key)

        result = set(chain.from_iterable(                  # Rassembler les doublons stocker dans le dictionnaire pour les afficher
            values for key, values in rev_dict.items()
            if len(values) > 1))
        # print(result)
        # printing result
        if str(result) == "set()":
            print("There are no duplicates in ", self.folder) # affichage des doublons
        else:
            print("The duplicates in ", self.folder, " are : ", str(result))
            print('____________________________________________________')
            val = input("Do you want to delete any of these files ? Y/N : ")
            val = str(val)[0].upper().strip()

            while val not in ['Y', 'N']:
                val = input("Input Yes (Y) or No (N) : ")

            if val == 'Y':
                to_delete = str(input("Which one do you want to delete ? "))
                li = os.listdir(self.folder)
                for j in li:                                                    # Suppression des doublons
                    file_name, extension = os.path.splitext(j)
                    if to_delete == j and j in result:
                        os.remove(self.folder + '/' + file_name + extension)
                        print(to_delete, " is deleted")
                        print('____________________________________________________')

    def do_all(self):
        start_time = time.time()                                    # Calcul de temps d'exécution
        self.clean_folder(input('Enter folder path : '))            # tri du dossier
        print("___________________ END OF EXECUTION _____________________")
        print("--------------------- %.2f seconds -----------------------" % (time.time() - start_time))


"""

# In C:/Users/Admin/Downloads

import Folder_Sorting_V_4

x = "C:/Users/Admin/Downloads"
a = Folder_Sorting_V_4.Folder(x)
#a.clean_folder(x) 
#a.do_all()        

"""
