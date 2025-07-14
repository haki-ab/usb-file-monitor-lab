import os
import time
import yagmail
from datetime import datetime

# 📁 Définir le lecteur USB à surveiller (par exemple "E:\")
usb_drive = "E:\\"

# 📍 Définir le chemin du fichier log local
log_file_path = "C:\\logs\\usb_activity.log"

# 📧 Configuration de l'e-mail
receiver = "PUT_EMAIL_HERE"  # 🔒 Remplacez ceci par l'adresse e-mail du destinataire
subject = "Alerte : Nouveau fichier copié vers USB"

# 🕒 Intervalle de vérification en secondes
interval = 5

# 📂 Créer un ensemble des fichiers déjà présents
existing_files = set(os.listdir(usb_drive)) if os.path.exists(usb_drive) else set()

# 🔁 Boucle infinie pour surveiller les changements
while True:
    if os.path.exists(usb_drive):
        current_files = set(os.listdir(usb_drive))
        new_files = current_files - existing_files

        if new_files:
            for file_name in new_files:
                log_entry = f"{datetime.now()} - Nouveau fichier détecté sur {usb_drive} : {file_name}\n"
                
                # 💾 Écrire l'entrée dans le fichier log
                with open(log_file_path, "a", encoding="utf-8") as log_file:
                    log_file.write(log_entry)
                
                # ✉️ Envoyer un e-mail avec le fichier détecté
                yag = yagmail.SMTP("PUT_EMAIL_HERE")  # 🔐 Remplacez avec votre e-mail d'envoi
                yag.send(
                    to=receiver,
                    subject=subject,
                    contents=log_entry
                )

        # Mettre à jour la liste des fichiers connus
        existing_files = current_files

    # ⏱️ Attendre avant la prochaine vérification
    time.sleep(interval)
