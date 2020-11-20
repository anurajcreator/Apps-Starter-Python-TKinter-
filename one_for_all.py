
import tkinter as tk
from tkinter import filedialog, Text, BOTTOM,RIGHT, LEFT
import os


root = tk.Tk()
root.title('One for All')
root.iconbitmap(r'icon.ico')
apps = []

if os.path.isfile('save.txt'):
    with open ('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

        
def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    try:
        initial = apps[len(apps)-1]
    except:
        initial = "/"
    
    filename=filedialog.askopenfilename(initialdir=initial, title="Selecfile",
                                      filetypes =(("executatbles", "*.exe"),("all files", " *.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        lable = tk.Label(frame, text=app, bg="gray")
        lable.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)
        
def clearApp():
    print('clear')
    for widget in frame.winfo_children():
        widget.destroy()
    apps.clear() 
    
    
canvas = tk.Canvas(root, height=700, width=700, bg='#3c6c80' )
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth = 0.8, relheight=0.8, relx = 0.1 , rely = 0.1)

openfile = tk.Button(root,text="Open File", padx=10, pady=5, fg="white", bg='#3c6c80', command= addApp)
openfile.pack(side = LEFT)

runapps = tk.Button(root,text="Run Apps", padx=10, pady=5, fg="white", bg='#3c6c80', command= runApps)
runapps.pack(side = LEFT)

clearAll = tk.Button(root,text="Clear Apps", padx=10, pady=5, fg="white", bg='#3c6c80', command= clearApp)
clearAll.pack(side = LEFT)
     
for app in apps:
        lable = tk.Label(frame, text=app, bg="gray")
        lable.pack()
    
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")

