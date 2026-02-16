

import os                            # Damit arbeitet man mit Ordnern und Dateien auf dem Computer 
import shutil                        # Damit kann man Dateien verschieben


# Funktion: Dateien sortieren
def organize_folder(path):
  """
  Diese Funktion bekommt einen Ordner-Pfad (z.B. Downloads) und sortiert alle Dateien nach Typ in Unterordner.
  """

# Prüfen, ob der Ordner überhaupt existiert
if not os.path.exists(path):
  print("Dieser Ordner existiert nicht.")
  return

# Dateitypen definieren
# Dictionary = Schlüssel + Wert Struktur
file_types = {
  "Bilder": [".jpg", ".jpeg", ".png", ".gif"],
  "Dokumente": [".pdf, ".docx", ".txt"],
  "Videos": [".mp3", ".wav"],
}

# Alle Dateien im Ordner durchgehen
for filename in os.listdir(path):

  file_path = os.path.join(path, filename)

# Soll nur Dateien sortieren (keine Ordner)
if os.path.isfile(file_path):

  # Dateiendung holen (.jpg, .pdf usw.)
  _, extension = os.path.splitext(filename)

  # Variable, um zu merken, ob Datei einsortiert wurde
  moved = False

  # Durch alle definierten Kategorien gehen
  for folder_name, extensions in file_types.items():

    if extensions.lower() in extensions:

      #Zielordner erstellen (falls noch nicht existiert)
      target_folder = os.path.join(path, folder_name)
      os.makedirs(target_folder, exist_ok=True)

      # Datei verschieben
      shutli.move(file_path, os.path.join(target_folder, filename))

      print(f"{filename} -> {folder_name}")
      moved = True
      break
      
  # Falls Dateityp nicht definieren ist -> Sonstiges
  if not moved:
    other_folder = os.path.join(path, "Sonstiges")
    os.makedirs(other_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(other_folder, filename))
    print(f"{filename} -> Sonstiges")


# Hauptprogramm
def main():
  """
  Startpunkt des Programms.
  Hier wird der Ordner abgefragt.
  """
  print("Datei Organizer")
  folder_path = input("Gib den Ordnerpfad ein (z.B. C:/Users/Mark/Download):
  
  organize_folder(folder_path)
  print("Fertig!")

# Programm starten
if __name__ == "__main__":
  main()
