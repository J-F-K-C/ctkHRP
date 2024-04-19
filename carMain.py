import customtkinter as ctk
import sqlite3

# Hauptfenster der Subanwendung
carMain_gui = ctk.CTk()
carMain_gui.geometry("1920x1080")
carMain_gui.title("Autoverwaltung")
ctk.set_appearance_mode("dark")

# Globale Variable zum Speichern des Index der ausgewählten Registerkarte
selected_tab_index = None

# Beenden der Anwendung
def exit_cars():
    carMain_gui.destroy()

# Verbindung zur Datenbank und Auslesen der Kerndaten
datenbankverbindung = sqlite3.connect("ctkHRP.db")
car_cursor = datenbankverbindung.cursor()
car_cursor.execute("SELECT COUNT(*) FROM Autos")
result = car_cursor.fetchone()
anzahl_der_Zeilen = result[0]
car_cursor.execute("SELECT Marke, Modell, Tankinhalt, Hubraum, PS, Besitzer, Kennzeichen FROM Autos")
cars_list = car_cursor.fetchall()

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

def show_fuel():
    # Fenster für Tankfüllungsdaten anzeigen
    show_fuel_window = ctk.CTkToplevel(master=carMain_gui)
    show_fuel_window.geometry("800x600")
    
    # Frame für Tankfüllungsdaten
    fuel_textbox = ctk.CTkTextbox(master=show_fuel_window, width=750, height=550)
    fuel_textbox.pack(side="top")
    
    # SQL-Abfrage für Tankfüllungsdaten basierend auf dem ausgewählten Kennzeichen ausführen
    selected_tab_name = car_tab.get()
    if selected_tab_name:
        selected_index = car_tab.index(selected_tab_name)
        print(f"Ausgewählte Registerkarte: {selected_tab_name} (Index: {selected_index})")
        
        # SQL-Statement zum Auslesen der Tankfüllungsdaten
        # Das Limit gibt an wieviele der letzten Zeilen ausgelesen werden sollen
        
        query = f"""
        SELECT Gesamtpreis, menge, Literpreis, Kilometerstand, Tankzeit
        FROM Tankfüllungen
        WHERE id = {selected_index}
        ORDER BY id DESC
        LIMIT 10 
        """
        car_cursor.execute(query)
        tank_data = car_cursor.fetchall()
        
        # Ergebnisse in die fuel_textbox einfügen
        for data in tank_data:
            gesamtpreis, menge, literpreis, kilometerstand, tankzeit = data
            fuel_textbox.insert("end", f"Gesamtpreis: {gesamtpreis}, Menge: {menge}, Literpreis: {literpreis}, Kilometerstand: {kilometerstand}, Tankzeit: {tankzeit}\n")
    else:
        print("Es wurde keine Registerkarte ausgewählt.")
    
    # Button zum Schließen des Fensters
    def exit_show_fuel():
        show_fuel_window.destroy()
    exit_show_fuel_button = ctk.CTkButton(master=show_fuel_window, text="Schließen", command=exit_show_fuel)
    exit_show_fuel_button.pack(side="right", padx=20)
    
    def add_fuel():
        add_fuel_window = ctk.CTkToplevel(master=show_fuel_window)
        add_fuel_window.geometry("640x480")
        # Eingabefelder für die Tankfüllungsdaten
        gesamtpreis = ctk.CTkEntry(master=add_fuel_window, placeholder_text="Gesamtpreis")
        gesamtpreis.pack(side="top", pady=20)
        menge = ctk.CTkEntry(master=add_fuel_window, placeholder_text="Menge")
        menge.pack(side="top", pady=20)
        literpreis = ctk.CTkEntry(master=add_fuel_window, placeholder_text="Literpreis")
        literpreis.pack(side="top", pady=20)
        kilometerstand = ctk.CTkEntry(master=add_fuel_window, placeholder_text="Kilometerstand")
        kilometerstand.pack(side="top", pady=20)
        tankzeit = ctk.CTkEntry(master=add_fuel_window, placeholder_text="Tankzeit")
        tankzeit.pack(side="top", pady=20)
        
        def save_fuel():
            # Werte aus den Eingabefeldern erhalten
            gesamtpreis_value = gesamtpreis.get()
            menge_value = menge.get()
            literpreis_value = literpreis.get()
            kilometerstand_value = kilometerstand.get()
            tankzeit_value = tankzeit.get()
            
            # SQL Statement zum einfügen der Werte in die Datenbank
            insert_fuel_values = f"""INSERT INTO Tankfüllungen (id, Gesamtpreis, menge, Literpreis, Kilometerstand, Tankzeit) VALUES ({selected_index}, {gesamtpreis_value}, {menge_value}, {literpreis_value}, {kilometerstand_value}, '{tankzeit_value}')"""
            
            try:
                # Datenbankverbindung herstellen und Cursor erstellen
                datenbankverbindung = sqlite3.connect("ctkHRP.db")
                car_cursor = datenbankverbindung.cursor()
            
                # Daten in die Datenbank einfügen
                car_cursor.execute(insert_fuel_values)
                datenbankverbindung.commit()
            
                # Erfolgsmeldung anzeigen
                print("Tankfüllungsdaten erfolgreich gespeichert!")
            except Exception as e:
                # Fehlermeldung anzeigen
                print(f"Fehler beim Speichern der Tankfüllungsdaten: {e}")
            finally:
                # Datenbankverbindung schließen
                datenbankverbindung.close()
            
        save_fuel_button = ctk.CTkButton(master=add_fuel_window, text="Speichern", command=save_fuel)
        save_fuel_button.pack(side="bottom", pady=10)
        # Beenden der Subanwendung zur Eingabe der Tankdaten
        def exit_add_fuel():
            add_fuel_window.destroy()
        exit_add_fuel_button = ctk.CTkButton(master=add_fuel_window, text="Abbrechen", command=exit_add_fuel)
        exit_add_fuel_button.pack(side="bottom", pady=10)
        
    
    add_fuel_button = ctk.CTkButton(master=show_fuel_window, text="Tankfüllung hinzufügen", command=add_fuel)
    add_fuel_button.pack(side="left", padx=20)
# Button zum Beenden der Anwendung
exit_button = ctk.CTkButton(master=carMain_gui, text="Beenden", command=exit_cars)
show_fuel_button = ctk.CTkButton(master=carMain_gui, text="Tankfüllungen anzeigen", command=show_fuel)

# Platzieren der Registerkarten und Einfügen von Buttons
car_tab.pack(side="top")
exit_button.pack(side="right", padx=20)
show_fuel_button.pack(side="left", padx=20)

carMain_gui.mainloop()
