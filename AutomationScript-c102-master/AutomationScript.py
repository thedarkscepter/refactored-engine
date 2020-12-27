import os
import shutil
import time

def backup_to_external_drive():
    source = input("Enter the DRIVE to be backed up: ")
    destination = "F:"

    source = source + '/'
    destination = destination + '/'

    list_of_files = os.listdir(source)

    seconds = time.time() - (30 * 24 * 60 * 60)


    if (seconds >= get_file_or_folder_age(source)):

        with open(source, 'rb') as f:  
            shutil.copy(source, destination)


def get_file_or_folder_age(path):

	ctime = os.stat(path).st_ctime

	return ctime


backup_to_external_drive()


