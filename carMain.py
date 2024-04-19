import customtkinter as ctk
import sqlite3

carMain_gui = ctk.CTk()
carMain_gui.geometry("1920x1080")
carMain_gui.title("Autoverwaltung")
ctk.set_appearance_mode("dark")

datenbankverbindung = sqlite3.connect("ctkHRP.db")
car_cursor = datenbankverbindung.cursor()
car_cursor.execute("SELECT COUNT(*) FROM Autos")
result = car_cursor.fetchone()
anzahl_der_Zeilen = result[0]
# print(anzahl_der_Zeilen)

car_cursor.execute("SELECT Marke, Modell, Tankinhalt, Hubraum, PS, Besitzer, Kennzeichen FROM Autos")

cars_list = car_cursor.fetchall()

# Listen zum Speichern der Werte für jede Spalte erstellen
marken = []
modelle = []
tankinhalte = []
hubraeume = []
ps_liste = []
besitzer_liste = []
kennzeichen_liste = []

def exit_cars():
    carMain_gui.destroy()

# Die Werte für jede Zeile in den entsprechenden Listen speichern
for row in cars_list:
    marke, modell, tankinhalt, hubraum, ps, besitzer, kennzeichen = row
    marken.append(marke)
    modelle.append(modell)
    tankinhalte.append(tankinhalt)
    hubraeume.append(hubraum)
    ps_liste.append(ps)
    besitzer_liste.append(besitzer)
    kennzeichen_liste.append(kennzeichen)
     

# Erzeugen der TabView
car_tab = ctk.CTkTabview(master=carMain_gui, width=1920, height=975)
car_tab.pack(padx=20, pady=20)


# Jedes Element erneut iterieren
for row in cars_list:
    marke, modell, tankinhalt, hubraum, ps, besitzer, kennzeichen = row
    
    # Registerkarte für jedes Auto erstellen
    tab = car_tab.add(kennzeichen)

    # Labels für die Autodaten in die Registerkarte einfügen
    ctk.CTkLabel(tab, text=f"Marke: {marke}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"Modell: {modell}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"Tankinhalt: {tankinhalt}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"Hubraum: {hubraum}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"PS: {ps}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"Besitzer: {besitzer}").pack(anchor="w")
    ctk.CTkLabel(tab, text=f"Kennzeichen: {kennzeichen}").pack(anchor="w")

exit_button = ctk.CTkButton(master=carMain_gui, text="Beenden", command=exit_cars)

# Platzieren Sie die Registerkarten und fügen Sie die Labels darunter ein
car_tab.pack(side="top")
labels_unten = ctk.CTkLabel(master=carMain_gui, text="")
labels_unten.pack(side="bottom")
exit_button.pack(side="bottom")
    


carMain_gui.mainloop()
