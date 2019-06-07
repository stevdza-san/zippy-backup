import os
import getpass
import shutil
import zipfile
import time

# Zippy (Windows OS) - Creates a backup of your files with the following extensions: .txt .pdf .docx .png .jpg
# which are located in the following directories: /Downloads /Desktop /Documents /Pictures
# in the lightning speed!

# Get Username.
username = getpass.getuser()

# Backup Directory Name.
backupDir = 'Backup-' + username

# PATH Variables
pathBackup = 'C:\\'
pathMyImages = pathBackup + backupDir + '\\Images'
pathMyDocuments = pathBackup + backupDir + '\\Documents'
pathLogFile = pathBackup + backupDir

pathDesktop = 'C:\\Users\\' + username + '\\Desktop\\'
pathDownloads = 'C:\\Users\\' + username + '\\Downloads\\'
pathDocuments = 'C:\\Users\\' + username + '\\Documents\\'
pathPictures = 'C:\\Users\\' + username + '\\Pictures\\'

# Navigate to Desktop and check if there is a backup directory.
# If there is not, the program will create one.
# If there is, the program will skip creating directory.
os.chdir(pathBackup)
backupDirExist = os.path.isdir(backupDir)
if not backupDirExist:
    print('Backup Directory:' + ' \'' + backupDir + '\' ' + 'Created on C: Partition')
    print('--------------------------------------------------------------------\n')
    os.mkdir(backupDir)
    os.mkdir(pathMyImages)
    os.mkdir(pathMyDocuments)

# LOG File
logfile = open(pathLogFile + '\\log.txt', 'a')


# BACKUP Images
def backup_images(folder, filename):
    if not folder.endswith('\\'):
        print('Copying \'' + folder + '\\' + filename + '\' to ' + pathMyImages)
        logfile.write('Copying \'' + folder + '\\' + filename + '\' to ' + pathMyImages + '\n')
        shutil.copy(folder + '\\' + filename, pathMyImages)
    else:
        print('Copying \'' + folder + filename + '\' to ' + pathMyImages)
        logfile.write('Copying \'' + folder + filename + '\' to ' + pathMyImages + '\n')
        shutil.copy(folder + filename, pathMyImages)


# BACKUP Documents
def backup_documents(folder, filename):
    if not folder.endswith('\\'):
        print('Copying \'' + folder + '\\' + filename + '\' to ' + pathMyDocuments)
        logfile.write('Copying \'' + folder + '\\' + filename + '\' to ' + pathMyDocuments + '\n')
        shutil.copy(folder + '\\' + filename, pathMyDocuments)
    else:
        print('Copying \'' + folder + filename + '\' to ' + pathMyDocuments)
        logfile.write('Copying \'' + folder + filename + '\' to ' + pathMyDocuments + '\n')
        shutil.copy(folder + filename, pathMyDocuments)


print('--------------------------------------------------------------------')
print('BACKUP The Following PATH: ' + pathDesktop)
print('--------------------------------------------------------------------')
time.sleep(1)
for folders, sub_folders, files in os.walk(pathDesktop):
    for eachFile in files:
        if eachFile.endswith('.txt'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.pdf'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.docx'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.jpg'):
            backup_images(folders, eachFile)
        elif eachFile.endswith('.png'):
            backup_images(folders, eachFile)

print('--------------------------------------------------------------------')
print('BACKUP The Following PATH: ' + pathDownloads)
print('--------------------------------------------------------------------')
time.sleep(1)
for folders, sub_folders, files in os.walk(pathDownloads):
    for eachFile in files:
        if eachFile.endswith('.txt'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.pdf'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.docx'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.jpg'):
            backup_images(folders, eachFile)
        elif eachFile.endswith('.png'):
            backup_images(folders, eachFile)

print('--------------------------------------------------------------------')
print('BACKUP The Following PATH: ' + pathDocuments)
print('--------------------------------------------------------------------')
time.sleep(1)
for folders, sub_folders, files in os.walk(pathDocuments):
    for eachFile in files:
        if eachFile.endswith('.txt'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.pdf'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.docx'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.jpg'):
            backup_images(folders, eachFile)
        elif eachFile.endswith('.png'):
            backup_images(folders, eachFile)

print('--------------------------------------------------------------------')
print('BACKUP The Following PATH: ' + pathPictures)
print('--------------------------------------------------------------------')
time.sleep(1)
for folders, sub_folders, files in os.walk(pathPictures):
    for eachFile in files:
        if eachFile.endswith('.txt'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.pdf'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.docx'):
            backup_documents(folders, eachFile)
        elif eachFile.endswith('.jpg'):
            backup_images(folders, eachFile)
        elif eachFile.endswith('.png'):
            backup_images(folders, eachFile)


logfile.close()
time.sleep(1)


def format_bytes(bytes_num):
    sizes = ["B", "KB", "MB", "GB", "TB"]

    i = 0
    dblbyte = bytes_num

    while i < len(sizes) and bytes_num >= 1024:
        dblbyte = bytes_num / 1024.0
        i = i + 1
        bytes_num = bytes_num / 1024

    return str(round(dblbyte, 2)) + " " + sizes[i]


total_size = 0
for path, dirs, files in os.walk(pathBackup + backupDir):
    for f in files:
        fp = os.path.join(path, f)
        total_size = total_size + os.path.getsize(fp)


print('\n\n*** Backup Successfully Created: ' + pathDesktop + ' ***')
print('*** Total Size: ' + format_bytes(total_size) + ' ***')

time.sleep(1)

# Archiving...
try:
    myArchive = zipfile.ZipFile(pathBackup + backupDir + '.zip', 'w')

    for one, two, three in os.walk(pathBackup + backupDir):
        for each_File in three:
            myArchive.write(os.path.join(one, each_File))

    myArchive.close()
    print('--------------------------------------------------------------------')
    print('*** Now Let\'s Archive Your Backup Files: ' + pathDesktop +backupDir + '.zip' + ' ***')
    shutil.move(pathBackup + backupDir, pathDesktop)
    shutil.move(pathBackup + backupDir + '.zip', pathDesktop)
except:
    print('--------------------------------------------------------------------')
    print('ERROR: Unable to Archive The Backup Directory (Try using Administrator Level Privilege.)')



