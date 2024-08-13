from tkinter import filedialog
import ttkbootstrap as ttk
import tools

filename = []
pages = []

def update_files():
    files = ""
    for i in range(0, len(filename)):
        if pages[i][0] == "a":
            files += "\n" + str(i + 1) + ". " + str(filename[i]) + ", all pages"
        else:
            files += "\n" + str(i + 1) + ". " + str(filename[i]) + ", p." + pages[i][0] + " - p." + pages[i][1]
    flabel.configure(text="Added:" + files)

def add_file():
    file = filedialog.askopenfilename(initialdir="C:/Users/", title="Select a File", filetypes=(("PDF files", "*.pdf*"),("All files", "*.*")))

    uinput = ptextbox.get("1.0", "end-1c").replace(" ", "").rsplit("-")

    if not file == "":
        if uinput[0].isdecimal() and len(uinput) == 2:
            if uinput[1].isdecimal():
                filename.append(file)
                pages.append(uinput)
                wlabel.configure(text="")
        elif uinput[0] == "a":
            filename.append(file)
            pages.append(uinput)
            wlabel.configure(text="")
        update_files()
    ptextbox.replace("1.0", "end-1c", "")


def create_pdf():
    oname = otextbox.get("1.0", "end-1c")
    if len(filename) == 0:
        wlabel.configure(text="No files have been added!")
    elif not len(oname) == 0:
        if tools.merge_pdf(filename, pages, oname):
            wlabel.configure(text=oname + ".pdf successfully created!")
            filename.clear()
            pages.clear()
            update_files()
            ptextbox.replace("1.0", "end-1c", "")
            otextbox.replace("1.0", "end-1c", "")
        else:
            wlabel.configure(text="Page numbers invalid!")
            filename.clear()
            pages.clear()
            update_files()
            ptextbox.replace("1.0", "end-1c", "")
            otextbox.replace("1.0", "end-1c", "")
    else:
        wlabel.configure(text="The output file has no name!")


root = ttk.Window(themename="litera")
root.title("SPM")
root.resizable(width=False, height=False)


hlabel = ttk.Label(root, text="Simple PDF Merger", font=('Arial', 20))
hlabel.grid(column=0, row=0)

llabel = ttk.Label(root, text="Please enter the page numbers (e.g. '3-8' or 'a' for all): ")
llabel.grid(column=0, row=1)

ptextbox = ttk.Text(root, width=15, height=1, wrap='word')
ptextbox.grid(column=1, row=1)

b1 = ttk.Button(root, text="Search file", width=30, command=add_file)
b1.grid(column=2, row=1)

flabel = ttk.Label(root, text="Added:", font=('Arial', 12))
flabel.grid(column=0, row=2)

olabel = ttk.Label(root, text="Output filename:", font=('Arial', 12))
olabel.grid(column=0, row=3)

otextbox = ttk.Text(root, width=15, height=1, wrap='word')
otextbox.grid(column=1, row=3)

b2 = ttk.Button(root, text="Create PDF", width=30, command=create_pdf)
b2.grid(column=2, row=3)

wlabel = ttk.Label(root, text=" ", font=('Arial', 12))
wlabel.grid(column=0, row=4)


root.mainloop()
