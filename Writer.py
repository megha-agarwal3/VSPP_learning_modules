import os
class filewriter:

    def __init__(self):
        self.name=input('Enter file name')
    
    
    def get_file_type(self):
        global file_extension
        file_extension = os.path.splitext(self.name)[1]
        print("Type of file:",file_extension)

    def open_file(self):
        global f
        f = open(self.name, 'w')
    
    def validate_file_type(self):
        print("Extension",file_extension)

        if file_extension==".txt":
            txt_input=input("Enter the input which we need to write in the file")
            f.write(txt_input)
            f.close()
            file1=open(self.name,'r')
            print(file1.read())

        if file_extension==".csv":
            pass

        if file_extension==".xlsx":
            pass

        if file_extension==".xml":
            pass

        if file_extension==".yaml":
            pass

w=filewriter()
w.get_file_type()
w.open_file()
w.validate_file_type()