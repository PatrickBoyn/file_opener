import os


def file_opener(*args):
    # List all of the files you want to open here. 
    files = []

    # For adding the arguments to the list.
    for a in args:
        files.append(a)

    # This is for opening all of my fsx files at once with one click.
    for a in files:
        os.startfile(a)
        print(a)


# Put the files paths in as parameters.
file_opener(r'E:\Steam\steamapps\common\FSX\fsx.exe',
            r'C:\Aerosoft\FSC9\FSC.exe', 
            r'C:\Program Files (x86)\HiFi\AS16_FSX\AS16.exe',
            r'C:\Program Files (x86)\rcv4x\rcv4.exe')
