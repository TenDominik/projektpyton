import tkinter
from tkinter import font
studenci=[]

def tworzstudent():
    student = {
        'imie': entry_imie.get(),
        'nazwisko': entry_nazwisko.get(),
        'plec': entry_plec.get(),
        'adres': entry_adres.get(),
        'rok_urodzenia': entry_rokur.get(),
        'kierunek': entry_kierunek.get(),
        'rok_studiow': entry_rok.get()
    }
    studenci.append(student)
    odswiezliste()

def czyszczenie():
    entry_imie.delete(0, tkinter.END)
    entry_nazwisko.delete(0, tkinter.END)
    entry_plec.delete(0, tkinter.END)
    entry_adres.delete(0, tkinter.END)
    entry_rokur.delete(0, tkinter.END)
    entry_kierunek.delete(0, tkinter.END)
    entry_rok.delete(0, tkinter.END)

def odswiezliste():
    lista.delete(1.0, tkinter.END)
    for student in studenci:
        lista.insert(tkinter.END, f"Imię: {student['imie']}, Nazwisko: {student['nazwisko']}, Płeć: {student['plec']}, Adres: {student['adres']}, Rok urodzenia: {student['rok_urodzenia']}, Kierunek: {student['kierunek']}, Rok studiów: {student['rok_studiow']}\n")

def szukajponazwisku():
    lista.delete(1.0, tkinter.END)
    for student in studenci:
        if student['nazwisko'].lower() == entry_search_nazwisko.get().lower():
            lista.insert(tkinter.END, f"Imię: {student['imie']}, Nazwisko: {student['nazwisko']}, Płeć: {student['plec']}, Adres: {student['adres']}, Rok urodzenia: {student['rok_urodzenia']}, Kierunek: {student['kierunek']}, Rok studiów: {student['rok_studiow']}\n")

def szukajporokuurodzonia():
    lista.delete(1.0, tkinter.END)
    for student in studenci:
        if str(student['rok_urodzenia']) == entry_search_rokur.get():
            lista.insert(tkinter.END, f"Imię: {student['imie']}, Nazwisko: {student['nazwisko']}, Płeć: {student['plec']}, Adres: {student['adres']}, Rok urodzenia: {student['rok_urodzenia']}, Kierunek: {student['kierunek']}, Rok studiów: {student['rok_studiow']}\n")

root = tkinter.Tk()
root.title("Baza danych studentów")
root.geometry("800x600")

tkinter.Label(root, text="Imię").grid(row=0, column=0)
entry_imie = tkinter.Entry(root, width=50)
entry_imie.grid(row=0, column=1, padx=10, pady=(10, 0))
tkinter.Label(root, text="Nazwisko").grid(row=1, column=0)
entry_nazwisko = tkinter.Entry(root, width=50)
entry_nazwisko.grid(row=1, column=1, padx=10)
tkinter.Label(root, text="Płeć").grid(row=2, column=0)
entry_plec = tkinter.Entry(root, width=50)
entry_plec.grid(row=2, column=1, padx=10)
tkinter.Label(root, text="Adres").grid(row=3, column=0)
entry_adres = tkinter.Entry(root, width=50)
entry_adres.grid(row=3, column=1, padx=10)
tkinter.Label(root, text="Rok urodzenia").grid(row=4, column=0)
entry_rokur = tkinter.Entry(root, width=50)
entry_rokur.grid(row=4, column=1, padx=10)
tkinter.Label(root, text="Kierunek").grid(row=5, column=0)
entry_kierunek = tkinter.Entry(root, width=50)
entry_kierunek.grid(row=5, column=1, padx=10)
tkinter.Label(root, text="Rok studiów").grid(row=6, column=0)
entry_rok = tkinter.Entry(root, width=50)
entry_rok.grid(row=6, column=1, padx=10)

tkinter.Button(root, text="Dodaj studenta", command=tworzstudent).grid(row=7, column=0, columnspan=2, pady=(20, 0))
tkinter.Button(root, text="Pokaż wszystkich studentów", command=odswiezliste).grid(row=8, column=0, columnspan=2, pady=(10, 0))

czcionka = font.Font(family="Helvetica", size=8)
lista = tkinter.Text(root, height=10, width=150, font=czcionka)
lista.grid(row=9, column=0, columnspan=2, pady=(20, 0))

tkinter.Label(root, text="Wyszukaj po nazwisku").grid(row=10, column=0, pady=(5, 0))
entry_search_nazwisko = tkinter.Entry(root, width=50)
entry_search_nazwisko.grid(row=10, column=1, padx=10)
tkinter.Button(root, text="Szukaj", command=szukajponazwisku).grid(row=11, column=0, columnspan=2)

tkinter.Label(root, text="Wyszukaj po roku urodzenia").grid(row=12, column=0, pady=(5, 0))
entry_search_rokur = tkinter.Entry(root, width=50)
entry_search_rokur.grid(row=12, column=1, padx=10)
tkinter.Button(root, text="Szukaj", command=szukajporokuurodzonia).grid(row=13, column=0, columnspan=2)

root.mainloop()