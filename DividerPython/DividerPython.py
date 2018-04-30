import os
import sys

def divide():
    print("divide")
    #give the path to the primary file
    path_p = input("Path: ")
    path_f = ''
    for letter in path_p:
        path_f = path_f + letter
        if letter == '\\':
            path_f = path_f + '\\'


    path_s = os.getcwd() + "\\output\\"
    file1 = open("file1",'wb')
    file2 = open("file2",'wb')
    end = b''

    flag = True

    with open(path,'rb') as file:
        byte = b'a'
        while byte != end:
            # Do stuff with byte.
            byte = file.read(1)
            if(flag):
                #write to file
                file1.write(byte)
                flag = False
            else:
                #write to another file
                file2.write(byte)
                flag = True
    file.close()
    file1.close()
    file2.close()
def merge():
    print("merge")

def main():
    print("Divide(d), merge(m) or exit(e)?")
    choice = ''
    while (choice!='d' and choice!='m' and choice!='e'):
        choice = input(">")
    if(choice=='e'):
        sys.exit()
    else:
        if(choice=='d'):
            divide()
        else:
            merge()

if __name__ =="__main__":
    main()