#fifth takes a list of md files and writes all headlines (lines starting with #) to a file
#Make sure your module can be called both from cli and imported to another module
#Create a new module that imports utils.py and test each function.
import os
import glob
def printDirNames(path, outputfile):
    """Takes path name of a directory and writes all the filenames to an outputfile given as input"""
    
    try:
        filenames = os.listdir(path)
        with open(outputfile, 'w') as file:
            file.writelines(filenames)
    except(OSError) as e:
        print(e)
    except(FileNotFoundError):
        print("File doesn't exist")

def printDirContents(dir, outputfile):
    """Takes path name of a directory and recursively writes all the filenames to an outputfile given as input"""

    try:
        filenames = glob.glob(pathname=dir + '/**/', recursive=True)
        with open(outputfile, 'w') as file:
            file.writelines(filenames)
    except(FileNotFoundError):
        print("File doesn't exist")
                


def printFileHeaders(path):
    """Prints the first line from a list of filenames"""
    try:
        filenames = os.listdir(path)
        for file in filenames:
            with open(path+file, 'r') as _file:
                lines = _file.readlines()
                print(lines[0])
    except(FileNotFoundError)as e:
        print(e)
        


def printEmail(path):
    """Checks a list of filenames for email addresses and prints them"""
    try:
        filenames = os.listdir(path)
        emailAddresses = []
        for file in filenames:
            if os.path.isdir(path+file):
                print(path + file + ' is a directory --- Skipping')
            else:
                with open(path+file, 'r') as _file:
                    lines = _file.readlines()
                    for line in lines:
                        if '@' in line:
                            emailAddresses.append(line)

        if(len(emailAddresses)==0):
            print('No email addresses found')
        else:
            print(emailAddresses)


    except(FileNotFoundError):
        print("File doesn't exist")

def printMarkDownHeaders(dir, outputfile):
    """Takes a list of md files and writes all headlines to a file specified"""
    try:
        headlines = []
        #Checks directory and subdirectories for files ending with .md
        filenames = glob.glob(pathname=dir + '/**/*.md', recursive=True)
        for file in filenames:
            print('Opening' + file)
            with open(file, 'r') as inputfile:
                lines = inputfile.readlines()
                for line in lines:
                    if '#' in line:
                        headlines.append(line) 

        with open(outputfile, 'w') as _outputfile:
            for headline in headlines:
                _outputfile.write(headline)
                _outputfile.write('\n')
    except(FileNotFoundError):
        print("File doesn't exist")
         



