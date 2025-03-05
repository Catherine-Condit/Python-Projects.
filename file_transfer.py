import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions destination button in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    #creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir Entry
        self.destination_dir.insert(0, selectDestDir)

    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #get the current time
        current_time = datetime.datetime.now()
        #use timedelta to subtract 24 hours (1 day) from the current time
        time_24_hours_ago = current_time - datetime.timedelta(days=1)
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            file_path = os.path.join(source, i)
            dest_file_path = os.path.join(destination, i)
            if not os.path.exists(dest_file_path):
                #if file does not exist in destination, it is considered new and can be added
                shutil.move(file_path, destination)
                print(f'{i} was successfully transferred as a new file.')
            else:            
                #get the last modified time of the file
                file_mod_time = os.path.getmtime(file_path)
                #convert file modification time to a datetime object
                file_mod_time = datetime.datetime.fromtimestamp(file_mod_time)
                #Check if the file's last modification time is within the last 24 hours
                if file_mod_time > time_24_hours_ago:
                    #check if the modified file is newer than the existing file at the destination
                    dest_file_mod_time = os.path.getmtime(dest_file_path)
                    dest_file_mod_time = datetime.datetime.fromtimestamp(dest_file_mod_time)
                    
                    if file_mod_time > dest_file_mod_time:
                        #if the source file is newer, replace the destination file
                        os.remove(dest_file_path)
                        shutil.move(file_path, destination)
                        print(f'{i} was successfully transferred as a modified file.')
                    else:
                        print(f'{i} is already up-to-date in the destination directory.')
                else:
                    print(f'{i} was not modified in the last 24 hours, so it was not transferred.')

    #creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

            

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
