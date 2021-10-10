import os
#  Permet l'utilisation des fonctionnalités dépendantes du système d'exploitation
# ( Dans ce code --> Manipuler les chemins des fichiers et leurs extensions)

import shutil
#  Manipulation de fichiers et de répertoires de haut niveau
# ( Dans ce code --> Déplacer les fichiers )

import hashlib
# Implémente une interface commune à de nombreux algorithmes de hachage sécurisés
# (Dans ce code --> utilisez sha256() pour créer un objet de hachage SHA-256 / Hachage des fichiers)

import sys
import time
# Calculer le temps d'exécution

import winshell
import ftplib
from datetime import datetime
from itertools import chain
# Créer une chaine à partir d'un itérable
import matplotlib.pyplot as plt


class Folder:

    def __init__(self, folder):  # Initialisation d'un objet (dossier) qu'on va trier
    def __init__(self, folder):
        self.folder = folder

    def clean_folder(self, folder):  # Chercher le dossier d'après le chemin saisi
    def clean_folder(self, folder):

        MT = 0
        print('_____________________________FINDING FOLDER______________________________')
        while not os.path.isdir(self.folder):
            print("Folder not found :( ", end='\n')
            self.folder = input(
                'Re-enter a valid folder path : ')  # Si on arrive pas à le trouver --> ressaisir le chemin
            input_time = time.time()
            self.folder = input('Re-enter a valid folder path : ')
            MT = (time.time() - input_time)
        else:
            print("Folder found !", end='\n')  # Si non on passe au tri du dossier
            print('____________________________________________________')
            self.sort_files(self.folder)
            print("Folder found !", end='\n')
            print('____________________________________________________________________')
            return MT

    def sort_files(self, folder):

        print('___________________________SORTING FOLDER______________________________')
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
            ext_list.append(str(extension))
            if extension in ext_list:
                if os.path.exists(self.folder + '/' + extension):                                  # True si chemin fait référence à un chemin existant ,False si non
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)    # Si le chemin est existant on y déplace le fichier
                    # shutil.move(src, dst, copy_function=copy2)
                if os.path.exists(self.folder + '/' + extension):
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)
                else:
                    os.makedirs(self.folder + '/' + extension)                                     # Si non on crée un répertoire
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)    # On y déplace le fichier
                    os.makedirs(self.folder + '/' + extension)
                    shutil.move(self.folder + '/' + i, self.folder + '/' + extension + '/' + i)

        print("Your files have been sorted")
        print("Your folder has been sorted")
        print("Current Folder -----> ", self.folder, " <-----")
        print('____________________________________________________')
        print('________________________________________________________________________')

        self.f_count(self.folder)          # Compter le nb de fichier / dossier
        self.after_sort(self.folder, li)   # Lister le contenu du dossier après le tri
        self.delete_folder(self.folder)    # Suppression des dossiers par extension
        self.after_sort(self.folder, li)
        self.graph(ext_list)
        return ext_list

    def f_count(self, folder):

        print('___________________________COUNTING FILES/FOLDERS_________________________')
        no_ext = 0
        total_files = 0
        total_dir = 0

        for base, dirs, files in os.walk(self.folder): # Parcourir le dossier parent
            # print('Searching in : ', base)
        for base, dirs, files in os.walk(self.folder):
            for directories in dirs:
                total_dir += 1           # Compter le nb de dossier
                total_dir += 1
            for Files in files:
                total_files += 1         # Compter le nb de fichier
                total_files += 1
                file_name, extension = os.path.splitext(Files)
                if extension == "":      # Trouver des fichiers sans extensions
                if extension == "":
                    no_ext += 1

        print("There is ", no_ext, "file(s) without extention(s)")
        print("Your total files", total_files)
        print("Your total folders", total_dir)
        print('____________________________________________________')
        print("There is ", no_ext, " file(s) without extention(s)")
        print("Your total files : ", total_files)
        print("Your total folders : ", total_dir)
        print('________________________________________________________________________')

    def after_sort(self, folder, li):

        print('___________________________NEW FOLDERS_________________________')
        print(len(li), "Folders recently created : ")
        li_ = os.listdir(self.folder)
        # Renvoie une liste contenant les noms des entrées (fichiers) dans le répertoire donné par chemin
        # Voir les dossiers récemment créés après le tri
        f = open('C:/Users/Admin/Desktop/Storage.txt', "a")
        f.write(self.folder + "\n")
        for i in li_:
            print("~ ", i, end="\n")
        print('____________________________________________________')

    def delete_folder(self, folder):

        val = input("Do you want to delete any of these folders ? Y/N : ")
        val = str(val)[0].upper().strip()
                                                                        # Voir si l'utilisateur veut supprimer
        while val not in ['Y', 'N']:                                    # un dossier en fonction des extensions

            val = input("Input Yes (Y) or No (N) : ")

        if val == 'Y':
            to_remove = input("Which extension ?  ")                    # choisir une extension
            self.folder2 = self.folder + '/' + str(to_remove)
            shutil.rmtree(self.folder2 )                                # suppression du dossier
            print(to_remove, "is deleted !")
            print('____________________________________________________')
            H = str(i) + '\n'
            f.write(H)
        f.close()
        print('_______________________________________________________________')

    # it doesn't work when there is an empty folders + if there are files that aren't sorted
    def delete_folder(self, v, li):

        print('___________________________DELETE FOLDERS BY EXTENSIONS_________________________')
        MT = 0
        input_time = time.time()
        v = str(v)[0].upper().strip()
        while v not in ['Y', 'N']:
            v = input("Input Yes (Y) or No (N) : ")
            v = str(v)[0].upper().strip()
        if v == 'N':
            return MT
        else:
            print("Alright Alright bye ...")
            print('____________________________________________________')

    def file_sha256(self, f_path):   # hachage des fichiers

        with open(f_path, "rb") as f:            # ouvrir le fichier
            file_hash = hashlib.sha256()         # utilisation de l'algorithme sha256 pour l'hachage du fichier
            while chunk := f.read(1024 * 1024):  # Lire un nombre d'octet du fichier
                file_hash.update(chunk)          
        return file_hash.hexdigest()             # Renvoie une valeur hexadécimale plus facile à manipuler 
            to_remove = input("Which extension ? ")
            while to_remove not in li:
                to_remove = input("Choose a valid extension from " + str(list(dict.fromkeys(li))) + " : ")
            else:
                MT = (time.time() - input_time)
                self.folder2 = self.folder + '/' + str(to_remove)
                f = open('C:/Users/Admin/Desktop/Deleted.txt', 'a')
                f.write(self.folder2)
                winshell.delete_file(self.folder2)
                f.close()
                print(to_remove, " is deleted successfully !")
                print('__________________________________________________________________________')
                self.delete_folder(input("Do you want to delete more folders ? Y/N : "),li)
                return MT

    # put deleted folders in deleted
    # other function to take the files out of the deleted folders in txt file qnd then delete them again
    def graph(self, x):
        print('______________________________GRAPH________________________________')
        start = time.time()
        conv = list(set(x))
        ExtensionsList = [conv]
        y = []
        for i in ExtensionsList[0]:
            n = x.count(i)
            y.append(n)

        plt.title("Number of Files")
        plt.xlabel('Files Extensions')
        plt.ylabel('Number')
        plt.yticks(y)
        plt.plot(conv, y, marker='o', c='g')
        plt.show()
        print("Time taken by the graph is  %2.f  ", time.time() - start, " seconds ")
        print('___________________________________________________________________')

    def file_sha256(self, f_path):
        with open(f_path, "rb") as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(1024 * 1024):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    def folder_hash(self, folder):
        print('___________________________FINDING DUPLICATES_________________________')
        MT = 0
        info = {}
        for file in os.listdir(self.folder):  #Parcourir les fichiers dans le dossier parent
            path = os.path.join(self.folder, file) # Jointure du chemin du dossier avec le fichier
            if os.path.isdir(path):    # si le chemin existe
                self.folder_hash(path)  # hachage en utilisant le chemin
        for file in os.listdir(self.folder):
            path = os.path.join(self.folder, file)
            if os.path.isdir(path):
                self.folder_hash(path)
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
                b = os.path.getsize(path)
                info[file] = (b, sha256)
        rev_dict = {}
        for key, value in info.items():
            rev_dict.setdefault(value, set()).add(key)

        result = set(chain.from_iterable(                  # Rassembler les doublons stocker dans le dictionnaire pour les afficher
        result = set(chain.from_iterable(
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
        self.delete_dup(result,input("Do you want to delete any of these files ? Y/N : "))
        return MT

            while val not in ['Y', 'N']:
                val = input("Input Yes (Y) or No (N) : ")

            if val == 'Y':
    #The duplicates in  C:/Users/Admin/Downloads  are :  {'hi - Copy.txt', 'hi.txt'} to fix
    # Which one do you want to delete ?  check if input is in result
    def delete_dup(self,result,v):
        if result:
            print("The duplicates in ", self.folder, " are : ", str(result))
            print('____________________________________________________________________')
            print('___________________________DELETING DUPLICATES_________________________')
            input_time = time.time()
            v = str(v)[0].upper().strip()
            while v not in ['Y', 'N']:
                v = input("Input Yes (Y) or No (N) : ")
                v = str(v)[0].upper().strip()
            if v == 'N':
                MT = (time.time() - input_time)
                return MT
            else:
                to_delete = str(input("Which one do you want to delete ? "))
                MT = (time.time() - input_time)
                li = os.listdir(self.folder)
                for j in li:                                                    # Suppression des doublons
                for j in li:
                    file_name, extension = os.path.splitext(j)
                    if to_delete == j and j in result:
                        os.remove(self.folder + '/' + file_name + extension)
                        f = open('C:/Users/Admin/Desktop/Deleted.txt', "a")
                        winshell.delete_file(self.folder + '/' + file_name + extension)
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y")  # %H:%M:%S
                        #f.write(self.folder + '/' + file_name + extension + " recycled at " + dt_string)
                        f.write(self.folder + '/' + file_name + extension)
                        f.write('\n')
                        f.close()
                        print(to_delete, " is deleted")
                        print('____________________________________________________')
                        print('____________________________________________________________________')
                        self.delete_dup(result,input("Do you want to delete more files ? Yes (Y) or No (N)"))
                        return MT
                else:
                    print("There are no duplicates in ", self.folder)
                    print('____________________________________________________________________')
                    return MT

    def check_if_sorted(self, folder):
        if os.path.exists('C:/Users/Admin/Desktop/Storage.txt'):
            for line in open('C:/Users/Admin/Desktop/Storage.txt', 'r'):
                if not self.folder == line:
                    print("This folder isn't sorted")
                    print('____________________________________________________')
                else:
                    print("This folder is already sorted")
                    print('____________________________________________________')
                    return True
        else:
            print("There is no history of sorting this file")
            return False

    def do_all(self):
        start_time = time.time()                                    # Calcul de temps d'exécution
        self.clean_folder(input('Enter folder path : '))            # tri du dossier
        print("___________________ END OF EXECUTION _____________________")
        print("--------------------- %.2f seconds -----------------------" % (time.time() - start_time))
    def history(self, folder):
        MT = 0
        input_time = time.time()
        val = input("Do u want to store data in a history file ? Y/N")
        val = str(val)[0].upper().strip()
        while val not in ['Y', 'N']:
            val = input("Input Yes (Y) or No (N) : ")
        if val == 'Y':
            HisPath = input("Where do you want to have the file ? ")
            while not os.path.isdir(HisPath):  # valid path and if history already exists or not
                print("Path not valid :( ", end='\n')
                HisPath = input('Re-enter a valid path : ')
            else:
                MT = (time.time() - input_time)
                if os.path.exists(str(HisPath) + '/' + 'History.txt'):
                    print("Valid path but History file already created", end='\n')
                    f = open(str(HisPath) + '/' + 'History.txt', "a")
                    f.write(self.folder)
                    f.close()
                    f = open("C:/Users/Admin/Desktop/Storage.txt", "a")
                    f.write(self.folder)
                    f.close()
                else:
                    MT = (time.time() - input_time)
                    print("Path found !", end='\n')
                    print('____________________________________________________')
                    f = open(str(HisPath) + '/' + 'History.txt', "a")
                    print("History.txt is created")
                    f.write(self.folder)
                    f.close()
                    f = open("C:/Users/Admin/Desktop/Storage.txt", "a")
                    f.write(self.folder)
                    f.close()
        else:
            MT = (time.time() - input_time)
            print("ALright no history then ")
            f = open("C:/Users/Admin/Desktop/Storage.txt", "a")
            f.write(self.folder)
            f.close()
        return MT

    def undo(self, root_path, cur_path):
        for filename in os.listdir(cur_path):
            if os.path.isfile(os.path.join(cur_path, filename)):
                shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
            elif os.path.isdir(os.path.join(cur_path, filename)):
                self.undo(root_path, os.path.join(cur_path, filename))
            else:
                sys.exit("Should never reach here.")


"""
    def empty_restored_folder(self, root_path, cur_path):
        for filename in os.listdir(cur_path):
            if os.path.isfile(os.path.join(cur_path, filename)):
                shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
            elif os.path.isdir(os.path.join(cur_path, filename)):
                self.empty_restored_folder(root_path, os.path.join(cur_path, filename))
            else:
                sys.exit("Should never reach here.")
        if cur_path != root_path:
            os.rmdir(cur_path)


    def del_new_folders(self):
        dir_li = []
        for line in open('C:/Users/Admin/Desktop/Storage.txt', 'r'):
            line = line[0:-1]
            dir_li.append(line)
        dir_li = dir_li[1:-1]
        for base, dirs, files in os.walk(self.folder):
            for directories in dirs:
                if directories in dir_li:
                    self.folder2 = self.folder + '/' + directories
                    os.rmdir(self.folder2)

    def restore_duplicates(self):

# In C:/Users/Admin/Downloads
        dictionnary = {}
        r = list(winshell.recycle_bin())  # returns list of objects of recycle-bin items
        print(r)
        for index, value in enumerate(r):
            dictionnary[index] = str(value)

import Folder_Sorting_V_4
        for line in open('C:/Users/Admin/Desktop/Deleted.txt', 'r'):
            string = str(line.replace('/','\\'))
            winshell.undelete(fr"{string}")
            if os.path.isdir(line):
                print('yes it is a folder')
                self.empty_restored_folder(self.folder,self.folder)

x = "C:/Users/Admin/Downloads"
a = Folder_Sorting_V_4.Folder(x)
#a.clean_folder(x) 
#a.do_all()        

"""
    def restore_deleted_folders(self):
        print("hi")

    def do_all(self):
        li = []
        start_time = time.time()
        input_time = time.time()
        folder = input('Enter folder path : ')
        while self.check_if_sorted(folder):
            folder = input("Choose a different folder path : ")
        else:
            MinusT = (time.time() - input_time)
            print("This folder isn't sorted")
            T1 = self.clean_folder(folder)
            self.f_count(self.folder)
            T2 = self.folder_hash(self.folder)
            li = self.sort_files(self.folder)
            T3 = self.delete_folder(input("Do you want to delete any of these folders ? Y/N : "), li)
            self.f_count(self.folder)
            T4 = self.history(self.folder)
            self.undo(folder, folder)
            self.del_new_folders()
            self.restore_duplicates()
            l = [T1, T2, T3, T4]
            for i in range(len(l)):
                if l[i] is None:
                    l[i] = 0
            RealT = (time.time() - start_time - (T1 - T2 - T3 - T4 - MinusT))
        print("___________________ END OF EXECUTION _____________________")
        print("Exec Time with input ")
        print("--------------------- %.2f seconds -----------------------" % (time.time() - start_time))  # with input
        print("Exec Time with graph without input ")
        print("--------------------- %.2f seconds -----------------------" % (time.time() - RealT))  # without input

# restore files in deleted folder and redelete the empty folder
