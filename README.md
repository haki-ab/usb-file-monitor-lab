# usb-file-monitor-lab
# USB File Monitor Lab – Hakim Abeoub

Ce projet démontre une solution simple et efficace pour surveiller la copie de fichiers vers des périphériques USB dans un environnement Windows Active Directory.

## 🎯 Objectif
- Détecter tout transfert de fichier vers un disque USB
- Enregistrer une alerte automatique dans un fichier partagé sur un serveur
- Fournir une preuve d’activité sans bloquer les actions de l’utilisateur

## ⚙️ Technologies utilisées
- PowerShell
- Windows 10/11
- Windows Server (partage SMB)
- Active Directory (facultatif)

## 🔧 Fonctionnement
1. Script PowerShell installé sur chaque poste client
2. Surveillance continue des nouveaux fichiers copiés vers D:\
3. Chaque événement est loggé dans un fichier centralisé : `\\DC1\SharedLogs\usb_alerts.log`

## 📸 Captures
📌 À ajouter :
- Fenêtre PowerShell pendant la surveillance
- Exemple d'entrée dans le fichier log
- Structure du dossier partagé

## 🧠 Auteur
Hakim Abeoub – passionné par les solutions simples, directes et applicables immédiatement en entreprise.
