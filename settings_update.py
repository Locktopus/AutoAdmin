#Modifying the "settings.py" file to production mode :

import lvar
import os

def main():

    fin = open(lvar.DEVELOPMENT_SETTINGS_FILE_PATH, "rt")
    fout = open("./settings.py", "wt")

    for line in fin:
        if "DEBUG" in line:
            fout.write(line.replace("True", "False"))
        elif "SECRET_KEY" in line:
            fout.write("SECRET_KEY = os.environ['SECRET_KEY']")
        elif "ALLOWED_HOSTS" in line:
            fout.write("ALLOWED_HOSTS = ['" + lvar.DOMAIN + "']")
        else:
            fout.write(line)
        
    fin.close()
    fout.close()