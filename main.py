"""
Fichier main du script d'automatisation de mise en production de site Django
"""
import shutil

chaine = "DEBUG"

shutil.copy("../locktopus/web_project/settings.py", "./settings.py")

fichier = open("./settings.py","r")
for ligne in fichier:
    if chaine in ligne:
        print(ligne)
fichier.close()