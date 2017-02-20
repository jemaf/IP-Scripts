#!/usr/bin/python

import sys
import os
import dropbox

def main(argv):

    if len(argv) < 3:
        print "Error: arguments not provided"
        exit(1)

    fileName = argv[1]
    path = argv[2]

    with open(fileName) as file: 
        for line in file:
            username = line.split(";")[0]
            email = line.split(";")[1]

            print "Processing student: " + username
            createFolder(path, username)

def createFolder(path, username):
    """Create a file

    Create a file using base path and username.
    Returns the folder's name if operation was successful
    """
    username = username.decode("utf-8").upper()

    filePath = path + "/" + username
    if not os.path.exists(filePath):
        os.makedirs(filePath)
        return filePath
    return None

if __name__ == "__main__":
    main(sys.argv)