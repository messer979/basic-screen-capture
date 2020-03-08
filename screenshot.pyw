import tkinter as tk
import pyautogui
import datetime, os


def cap_screen():
    now = datetime.datetime.now()
    suffix = now.strftime('%m-%d-%H%M%S')
    screenshot = pyautogui.screenshot()
    screenshot.save(r"C:\Users\Rachel\Desktop\Screenshots\capture-%s.png" % (suffix))

def delete_old_files():
    compare_date = datetime.datetime.now() - datetime.timedelta(days=45) 
    for file in os.scandir():
        create_time = datetime.datetime.utcfromtimestamp(file.stat().st_mtime)
        if create_time < compare_date:
            os.remove(file)

root = tk.Tk()
root.minsize(300, 70)
#tk.PhotoImage(file='')
#root.iconbitmap(r'C:\Users\Rachel\Documents\ScreenCapture\icon.ico')
root.tk.call('wm', 'iconbitmap', root._w, 'icon.ico')
root.title('Capture Screen Program')
root.configure(background='black')

btn = tk.Button(root, text='Capture Screen', command = cap_screen)
btn.pack(anchor='center', pady='15')

dbtn = tk.Button(root, text='Clean', command = delete_old_files)
dbtn.pack(anchor='se', pady='5', padx='2')


root.mainloop()
