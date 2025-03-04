import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #row and column weights grid config to make window more responsive
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)
        

        #custom text input label and entry widget
        self.text_label = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.text_entry = Entry(self.master)
        self.text_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        self.generate_default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.generate_default_btn.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        self.generate_custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.generate_custom_btn.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

    def defaultHTML(self):
        #get default text if user chooses default html page
        defaultText = "Stay tuned for our amazing summer sale!"
        #write HTML content to file
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + defaultText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        #open in default browser
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        #get custom text input from entry widget
        customText = self.text_entry.get()
        #use default message if nothing is entered
        if customText.strip() =="":
            customText ="Please enter custom text into the Web Page Generator to see it displayed here!"
        #write HTML content to file
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        #open in default browser
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


