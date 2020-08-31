import argparse
import csv
import sys, getopt

#create a helper function that gets an arbitrary number of strings instead of a list
def convertStringsToList(string):
    convertedList = string.split(' ')
    return convertedList


#def print_file_content(file) that can print content of a text file to the console
def printFile(inputfile):
    try:
        with open(inputfile, 'r') as _inputfile:
            output = _inputfile.readlines()
            print(output)
    except(FileNotFoundError):
        print("File doesn't exist")
        
#def write_list_to_file(output_file, lst) that can take a list or tuple and
#write each element to a new line in file
def writeListToFile(outputFile, lst):
    try:
        with open(outputFile, 'a') as _outputFile:
            for item in lst:
                _outputFile.write(item)
            _outputFile.write('\n')
    except(FileNotFoundError):
        print("File doesn't exist")
        
#def read_file(input_file) that take a csv file and read each row into a list
def readFile(inputFile):
    try:
        with open(inputfile, newline='') as csvFile:
            reader = csv.reader(csvFile, delimeter=',')
            for row in reader:
                print(row)
        
    except(FileNotFoundError):
        print("File doesn't exist")
    

#Add a functionality so that the program can be called from cli with 2 arguments
#path to input file
#an argument --file file_name to be used as the output file to write to.
#if only the input file is given write output to console
#if the input file is given with a list of extra words add those words to the output (whether to file or console)
#Add 'help' attributes to each cli argument to describe how the module is used 

# Initiate the parser
parser = argparse.ArgumentParser()
#parser.add_argument("-h", "--help", help="This command prints the help", action="store_true")
parser.add_argument("-f", "--file", help="This command reads a file")
parser.add_argument("-w", "--words", help="This command lets you append words to a file given with the -w parameter")
# Read arguments from the command line
args = parser.parse_args()

if args.file:
    printFile(args.file)

if args.file and args.words:
    writeListToFile(args.file, args.words)
    printFile(args.file)

