import os
#  Permet l'utilisation des fonctionnalités dépendantes du système d'exploitation
# ( Dans ce code --> Manipuler les chemins des fichiers et leurs extensions)

import shutil
#  Manipulation de fichiers et de répertoires de haut niveau
# ( Dans ce code --> Déplacer les fichiers )

dirName = input('Enter folder path : ')
# Saisie du chemin du fichier qu'on veut filtrer


li = os.listdir(dirName)
# Renvoie une liste contenant les noms des entrées (fichiers) dans le répertoire donné par chemin
# exemple : ['Convention de stage.xlsx', 'python-3.9.6-amd64.exe','Sujet_de_stage.pdf']


for i in li:
    # Parcourir la liste contenant les  noms des entrées

    fileName, extension = os.path.splitext(i)
    # Séparation des extensions des noms des fichiers en une paire (racine, ext)
    # racine + ext == chemin du fichier
    # ext soit vide ou commence par un point et contienne au plus un point.

    extension = extension[1:] # Enlever le (.)

    if extension == "":  # On passe au cas d'abscence d'extension
        continue

    if os.path.exists(dirName + '/' + extension):                               # True si chemin fait référence à un chemin existant ,False si non
        shutil.move(dirName + '/' + i, dirName + '/' + extension + '/' + i)     # Si le chemin est existant on y déplace le fichier
                   # shutil.move(src, dst, copy_function=copy2)
    else:
        os.makedirs(dirName + '/' + extension)                                  # Si non on crée un répertoire
        shutil.move(dirName + '/' + i, dirName + '/' + extension + '/' + i)     # On y déplace le fichier
