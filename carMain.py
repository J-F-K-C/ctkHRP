import customtkinter as ctk
import sqlite3

carMain_gui = ctk.CTk()
carMain_gui.geometry("1920x1080")
carMain_gui.title("Autoverwaltung")
ctk.set_appearance_mode("dark")

datenbankverbindung = sqlite3.connect("OpenHRP.db")
car_cursor = datenbankverbindung.cursor()
car_cursor.execute("SELECT COUNT(*) FROM Autos")
result = car_cursor.fetchone()
anzahl_der_Zeilen = result[0]
print(anzahl_der_Zeilen)

car_cursor.execute("SELECT Marke, Modell, Tankinhalt, Hubraum, PS FROM Autos")

cars_list = car_cursor.fetchall()

# Liste zum Speichern der Tupel erstellen
tupel_liste = []

# Die Einträge jeder Zeile in einem Tupel speichern
for row in cars_list:
    marke, modell, tankinhalt, hubraum, ps = row
    
    # Hier können Sie mit den Variablen arbeiten, z.B. drucken:
    print("Marke:", marke)
    print("Modell:", modell)
    print("Tankinhalt:", tankinhalt)
    print("Hubraum:", hubraum)
    print("PS:", ps)
    print()  # Leerzeile für bessere Lesbarkeit


car_tab = ctk.CTkTabview(master=carMain_gui, width=1920, height=1080)
car_tab.pack(padx=20, pady=20)

for row in cars_list:
    car_tab.add(marke)







carMain_gui.mainloop()