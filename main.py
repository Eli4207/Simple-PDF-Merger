import os.path
from tkinter import filedialog
from functools import partial
import ttkbootstrap as ttk
import tools

filename = []
pages = []
rpages = []
mergelist = []
buttonlist = []

def update_files():
    for file in mergelist:
        file.destroy()
    mergelist.clear()
    for button in buttonlist:
        button.destroy()
    buttonlist.clear()

    if len(pages) > 0:
        for i in range(0, len(filename)):
            if pages[i][0] == "a":
                mergelist.append(ttk.Label(root, text=str(i + 1) + ". " + str(filename[i]) + ", all pages" + "\n", font=('Arial', 12)))
                mergelist[i].grid(column=0, row=3 + i)
            else:
                mergelist.append(ttk.Label(root, text=str(i + 1) + ". " + str(filename[i]) + ", p." + pages[i][0] + " - p." + pages[i][1] + "\n", font=('Arial', 12)))
                mergelist[i].grid(column=0, row=3 + i)
            buttonlist.append(ttk.Button(root, text="Delete", width=10, padding=5, command=partial(delete, i)))
            buttonlist.append(ttk.Button(root, text="Down", width=10, padding=5, command=partial(move_down, i)))
            buttonlist.append(ttk.Button(root, text="Up", width=10, padding=5, command=partial(move_up, i)))
            buttonlist[i * 3].grid(column=3, row=3 + i, columnspan=4, sticky=ttk.W)
            buttonlist[i * 3 + 1].grid(column=3, row=3 + i, columnspan=4)
            buttonlist[i * 3 + 2].grid(column=3, row=3 + i, columnspan=4, sticky=ttk.E)
            if len(filename) == 1:
                buttonlist[i * 3 + 1].grid_forget()
                buttonlist[i * 3 + 2].grid_forget()
            elif i == len(filename) - 1:
                buttonlist[i * 3 + 1].grid_forget()
            elif i == 0:
                buttonlist[i * 3 + 2].grid_forget()

    olabel.grid(column=1, row=len(mergelist)+4)
    otextbox.grid(column=1, row=len(mergelist)+4)
    b2.grid(column=2, row=len(mergelist)+4)
    wlabel.grid(column=0, row=len(mergelist)+5)

def add_file():
    file = filedialog.askopenfilename(initialdir=os.path.abspath(__file__), title="Select a File", filetypes=(("PDF files", "*.pdf*"),("All files", "*.*")))

    uinput = ptextbox.get("1.0", "end-1c").replace(" ", "").rsplit("-")

    if not (str(file) == "" or str(file) == "()"):
        if uinput[0].isdecimal() and len(uinput) == 2:
            if uinput[1].isdecimal():
                filename.append(file)
                pages.append(uinput)
                rpages.append(r.get())
                wlabel.configure(text="")
        elif uinput[0] == "a":
            filename.append(file)
            pages.append(uinput)
            rpages.append(r.get())
            wlabel.configure(text="")
        update_files()
    ptextbox.replace("1.0", "end-1c", "")

def delete(i):
    filename.pop(i)
    pages.pop(i)
    rpages.pop(i)
    update_files()

def move_up(i):
    temp_filename = filename[i]
    filename[i] = filename[i - 1]
    filename[i - 1] = temp_filename

    temp_pages = pages[i]
    pages[i] = pages[i - 1]
    pages[i - 1] = temp_pages

    temp_rpages = rpages[i]
    rpages[i] = rpages[i - 1]
    rpages[i - 1] = temp_rpages

    update_files()

def move_down(i):
    temp_filename = filename[i]
    filename[i] = filename[i + 1]
    filename[i + 1] = temp_filename

    temp_pages = pages[i]
    pages[i] = pages[i + 1]
    pages[i + 1] = temp_pages

    temp_rpages = rpages[i]
    rpages[i] = rpages[i + 1]
    rpages[i + 1] = temp_rpages

    update_files()

def create_pdf():
    oname = otextbox.get("1.0", "end-1c")

    if len(filename) == 0:
        wlabel.configure(text="No files have been added!")
    elif not len(oname) == 0:
        if tools.merge_pdf(filename, pages, rpages, oname):
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
r = ttk.IntVar()


hlabel = ttk.Label(root, text="Simple PDF Merger", font=('Arial', 20))
hlabel.grid(column=0, row=0)

llabel = ttk.Label(root, text="Please enter the page numbers (e.g. '3-8' or 'a' for all): ", font=('Arial', 12))
llabel.grid(column=0, row=1)

ptextbox = ttk.Text(root, width=15, height=1, wrap='word')
ptextbox.grid(column=1, row=1)

b1 = ttk.Button(root, text="Search file", width=30, command=add_file)
b1.grid(column=2, row=1, padx=8)

rlabel = ttk.Label(root, text="Rotation (clockwise): ", font=('Arial', 12))
rlabel.grid(column=0, row=2)

r1 = ttk.Radiobutton(root, text="0°", variable=r, value=0, state="normal")
r1.grid(column=3, row=2, padx=20)

r2 = ttk.Radiobutton(root, text="90°", variable=r, value=90)
r2.grid(column=4, row=2, padx=20)

r3 = ttk.Radiobutton(root, text="180°", variable=r, value=180)
r3.grid(column=5, row=2, padx=20)

r4 = ttk.Radiobutton(root, text="270°", variable=r, value=270)
r4.grid(column=6, row=2, padx=20)

flabel = ttk.Label(root, text="Added:", font=('Arial', 12))
flabel.grid(column=0, row=3)

olabel = ttk.Label(root, text="Output filename:", font=('Arial', 12))
olabel.grid(column=0, row=4, padx=8)

otextbox = ttk.Text(root, width=15, height=1, wrap='word')
otextbox.grid(column=1, row=4)

b2 = ttk.Button(root, text="Create PDF", width=30, command=create_pdf)
b2.grid(column=2, row=4)

wlabel = ttk.Label(root, text=" ", font=('Arial', 12))
wlabel.grid(column=0, row=5)


root.mainloop()
