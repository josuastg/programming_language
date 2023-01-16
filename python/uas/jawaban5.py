# Heading
import tkinter as tk
from tkinter import ttk #Frame Input
from tkinter.messagebox import showinfo #Import Display Show Info

# init
window = tk.Tk()
window.configure(bg="black")
window.geometry("400x400")
window.resizable(False, False)
window.title("INPUT DATA KENDARAAN")

# Variabel dan Fungsi
vehicleName = tk.StringVar()
regNumber = tk.StringVar()

# Frame Input
input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


# 1. Label Tipe/Merk Kendaraan
vehicleNameLabel = ttk.Label(input_frame,text="Tipe/Merk Kendaraan: ")
vehicleNameLabel.pack(padx=10,fill="x",expand=True)

# 2. Input Tipe/Merk Kendaraan
vehicleNameInput = ttk.Entry(input_frame,textvariable=vehicleName)
vehicleNameInput.pack(padx=10,fill="x",expand=True)

# 1. Label Nomor Kendaraan
regNumberLabel = ttk.Label(input_frame,text="Nomor Kendaraan: ")
regNumberLabel.pack(padx=10,fill="x",expand=True)

# 2. Input Tipe/Merk Kendaraan
regNumberInput = ttk.Entry(input_frame,textvariable=regNumber)
regNumberInput.pack(padx=10,fill="x",expand=True)

def submit():

    pesan = f"""
    Terimakasih tipe/merk kendaraan {vehicleName.get()} 
    dengan no. registrasi {regNumber.get()} berhasil diinput !"""
    showinfo(title="HASIL",message=pesan)

clickSubmit = ttk.Button(input_frame,text="Submit",command=submit)
clickSubmit.pack(fill='x',expand=True,padx=10,pady=10)


window.mainloop()
