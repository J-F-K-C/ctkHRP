import customtkinter as ctk
import subprocess

# GUI Erstellung
main_gui = ctk.CTk()
main_gui.title("OpenHRP")
ctk.set_appearance_mode("dark")
main_gui.geometry("2000x50")

# Öffnet das Modul zur Autoverwaltung
def cars_module():
    subprocess.Popen(["python", "carMain.py"])

# Beendet die Anwendung
def exit_button():
    main_gui.destroy()


# Öffnet das Modul zur Autoverwaltung
cars_module_button = ctk.CTkButton(master=main_gui, text="Autoverwaltung", command=cars_module)
cars_module_button.grid(row=0, column=0, pady=5, padx=5)


# Beenden Button, Column verschieben wenn neuer Button hinzugefügt wird
exit_button = ctk.CTkButton(master=main_gui, text="Beenden", command=exit_button)
exit_button.grid(row=0, column=1, pady=5, padx=5)

main_gui.mainloop()