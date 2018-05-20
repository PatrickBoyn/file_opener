import os


class FileOpener:
    # List all of the files you want to open here. 
    files = [
        r'E:\Steam\steamapps\common\FSX\fsx.exe',
        r'C:\Aerosoft\FSC9\FSC.exe',
        r'C:\Program Files (x86)\HiFi\AS16_FSX\AS16.exe',
        r'C:\Program Files (x86)\rcv4x\rcv4.exe'
    ]

    # This function runs the files
    # The best way of doing this is passing a list.
    def open_file(ls):
        os.startfile(ls)
    

    # This is for opening all of my fsx files at once with one click. 
    for a in files:
        open_file(a)
        print(a)


FileOpener()
