import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

# Inisialisasi
window = tkinter.Tk()
window.configure(bg="teal")
window_icon = file=PhotoImage(file='assets/mukbang.png')
window.iconphoto(False, window_icon)
window.geometry("400x370")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")

# Header
header_label = ttk.Label(window, text="Pengisian Formulir", font="Arial 16 bold", background="teal", foreground="white")
header_label.pack(pady=20)

# Variabel dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()
OLAHRAGA_FAVORIT = tkinter.StringVar()

# Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not ALAMAT.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get() or not OLAHRAGA_FAVORIT.get():
    showinfo(title="Error!", message="Mohon lengkapi semua data!")
 else:
    pesan = f"Hallo {NAMA_LENGKAP.get()}, kamu berhasil mendaftar dengan data sebagai berikut:\n\nNama Lengkap: {NAMA_LENGKAP.get()}\nAlamat: {ALAMAT.get()}\nMakanan Favorit: {MAKANAN_FAVORIT.get()}\nMinuman Favorit: {MINUMAN_FAVORIT.get()}\nOlahraga Favorit: {OLAHRAGA_FAVORIT.get()}\n\nTerimakasih telah mendaftar."
    showinfo(title="Selamat", message=pesan)

# frame input
style = ttk.Style()
style.configure(style="Custom.TEntry", fieldbackground="green")
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# component nama lengkap
nama_depan_label = ttk.Label(input_frame, text="Nama lengkap:")
nama_depan_label.pack(padx=10, fill="x", expand=True)
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_LENGKAP, style="Custom.TEntry", font="Calibri 12 bold")
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# component alamat
alamat_rumah_label = ttk.Label(input_frame, text="Alamat:")
alamat_rumah_label.pack(padx=10, fill="x", expand=True)
alamat_rumah_entry = ttk.Entry(input_frame, textvariable=ALAMAT, font="Calibri 12 bold")
alamat_rumah_entry.pack(padx=10, fill="x", expand=True)
# component makanan favorit
makanan_favorit_label = ttk.Label(input_frame, text="Makanan Favorit:")
makanan_favorit_label.pack(padx=10, fill="x", expand=True)
makanan_favorit_entry = ttk.Entry(input_frame, textvariable=MAKANAN_FAVORIT, font="Calibri 12 bold")
makanan_favorit_entry.pack(padx=10, fill="x", expand=True)
# component minuman favorit
minuman_favorit_label = ttk.Label(input_frame, text="Minuman Favorit:")
minuman_favorit_label.pack(padx=10, fill="x", expand=True)
minuman_favorit_entry = ttk.Entry(input_frame, textvariable=MINUMAN_FAVORIT, font="Calibri 12 bold")
minuman_favorit_entry.pack(padx=10, fill="x", expand=True)
# component olahraga favorit
olahraga_favorit_label = ttk.Label(input_frame, text="Olahraga Favorit:")
olahraga_favorit_label.pack(padx=10, fill="x", expand=True)
olahraga_favorit_entry = ttk.Entry(input_frame, textvariable=OLAHRAGA_FAVORIT, font="Calibri 12 bold")
olahraga_favorit_entry.pack(padx=10, fill="x", expand=True)

# tombol
tombol_daftar = ttk.Button(input_frame, text="Daftar", command=tombol_click)
tombol_daftar.pack(padx=10, pady=10, fill="x", expand=True)


window.mainloop()