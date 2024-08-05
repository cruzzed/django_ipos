import datetime
import django
import os
from django.utils.timezone import now
import dotenv
dotenv.read_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_ipos.settings')
django.setup()

from django.db.models import Sum, Count

from ipos.models import TblIkhd, TblUser

import tkinter as tk
from tkinter import messagebox

debug = True

def login_form():

    window = tk.Tk()
    window.title("Login")

    frm_login = tk.Frame(relief=tk.FLAT, borderwidth=3)
    frm_login.pack()

    lbl_username = tk.Label(master=frm_login, text="User:")
    lbl_username.pack(side=tk.LEFT)

    txt_username = tk.Entry(master=frm_login)
    txt_username.pack(side=tk.LEFT)

    btn_login = tk.Button(master=frm_login, text="Login")
    btn_login.pack(side=tk.LEFT)

    # Bind keypress event to handle_keypress()

    def login(event):
        
        global user1
        user1 = txt_username.get().upper()
        window.destroy()
     
    def on_closing():
        if messagebox.askokcancel("Keluar", "Keluar?"):
            window.destroy()
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    btn_login.bind("<Button-1>", login)
    window.bind("<Return>", login)
    window.after(1, lambda: window.focus_force())
    window.mainloop()
    print(user1)
    return user1
    
while True:
    user1 = login_form()
    if not user1 or TblUser.objects.filter(userid=user1).count() == 0:
        if not messagebox.askokcancel("User Error", "Ulangi?"):
            exit()
    else:
        popup = messagebox.showinfo(
            title="Login Sukses!",
            message=f'Selamat Datang, {user1}',
        )
        break

total_rekap = (
    TblIkhd.objects
        .filter(tanggal__range=(now().date(), (now().date()+ datetime.timedelta(days=1) )))
        .filter(user1=user1)
        .filter(kantordari="UTM")
        .filter(tipe__in=("KSR", "TRBCIMPKSR"))
        .values("tanggal")
)

totalakhir = total_rekap.aggregate(Sum("totalakhir"))["totalakhir__sum"]

if not totalakhir and not debug:
    raise Exception("Tidak ditemukan penjualan pada hari ini.")

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Formulir Isi Kasir")
window.lift()
window.attributes("-topmost", True)


# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

lbl_tgl = tk.Label(master=frm_form, text="Tanggal:")
ent_tgl = tk.Label(
    master=frm_form, 
    text=now().strftime("%d-%m-%Y") #today_TblIkhd.tanggal
)
lbl_tgl.grid(row=0, column=0, sticky="e")
ent_tgl.grid(row=0, column=1, sticky="")

# List of field labels
nominals = [
    100000, 75000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 1
]

entries = []

# Loop over the list of field labels
for idx, nominal in enumerate(nominals):
    idx += 1
    # Create a Label widget with the text from the labels list
    if nominal == 1:
        label = tk.Label(master=frm_form, text=f"Non-tunai")
    else:
        label = tk.Label(master=frm_form, text=f"Rp. {nominal:,}")
    # Create an Entry widget
    entry = tk.Entry(master=frm_form, width=50)
    entries.append(entry)
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the row whose index is idx
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
def submit(event):
    total = 0
    for idx in range(len(nominals)):
        val = entries[idx].get().strip()           
        if not val:
            continue
        else:
            print(f'{int(val)} * {int(nominals[idx])} = {nominals[idx] * int(val)}')
            total += nominals[idx] * int(val)
            print(f'{total - (nominals[idx] * int(val))} + {nominals[idx] * int(val)} = {total}')
    result = total - int(totalakhir)
    print(f'{total} - {int(totalakhir)} = {total - int(totalakhir)}')
    if result <= -500000:
        conclusion = f"Kurang, Mohon dihitung ulang dengan lebih seksama dan pastikan input nominal anda sesuai, setelah itu Submit ulang."
    elif result < 0:
        conclusion = f"Kurang: {int(result * -1):,}"
    else:
        conclusion = f"Lebih: {int(result):,}"
    
    popup = messagebox.showinfo(
        master=window,
        title="Hasil",
        message=conclusion,
    )
    
def on_closing(event=None):
    if messagebox.askokcancel("Keluar", "Keluar?"):
        from pathlib import Path
        script_dir = Path(__file__).parent.absolute()
        print(script_dir)
        with open(f'{script_dir}\log{now().date().strftime("%d%m%Y")}.txt', 'w+') as log:
            print(log)
            total = 0
            for idx in range(len(nominals)):
                val = entries[idx].get().strip()           
                if not val:
                    continue
                else:
                    log.write(f'{int(val)} * {int(nominals[idx])} = {nominals[idx] * int(val)}\n')
                    total += nominals[idx] * int(val)
                    log.write(f'{total - (nominals[idx] * int(val))} + {nominals[idx] * int(val)} = {total}\n')
            result = total - int(totalakhir)
            log.write(f'{total} - {int(totalakhir)} = {total - int(totalakhir)}\n')
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.bind("<Return>", submit)
btn_submit = tk.Button(master=frm_buttons, text="Submit", )
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_submit.bind("<Button-1>", submit)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_cancel = tk.Button(master=frm_buttons, text="Keluar")
btn_cancel.pack(side=tk.RIGHT, ipadx=10)
btn_cancel.bind("<Button-1>", on_closing)

# Start the application
window.after(1, lambda: window.focus_force())
window.mainloop()
