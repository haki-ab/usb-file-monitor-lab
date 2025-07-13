# 📍 Chemin à surveiller (clé USB)
$watchPath = "E:\"

# 📍 Chemin du fichier de log sécurisé
$logFile = "C:\log\usb_log.txt"

# 📍 Types de fichiers sensibles à surveiller
$filter = "*.docx","*.xlsx","*.pdf","*.zip"

# 🔐 Crée le dossier de log s'il n'existe pas
if (-not (Test-Path "C:\log")) {
    New-Item -Path "C:\log" -ItemType Directory
}

# 📂 Liste précédente des fichiers (pour comparer)
$lastFiles = @()

Write-Host "✅ Surveillance démarrée sur $watchPath"
Write-Host "📄 Les événements seront enregistrés dans: $logFile"

while ($true) {
    if (Test-Path $watchPath) {
        $currentFiles = Get-ChildItem -Path $watchPath -Recurse -Include $filter -ErrorAction SilentlyContinue
        $newFiles = $currentFiles | Where-Object { $lastFiles -notcontains $_.FullName }

        foreach ($file in $newFiles) {
            $time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $user = $env:USERNAME
            $log  = "$time [$user] Nouveau fichier détecté: $($file.FullName)"
            Add-Content -Path $logFile -Value $log
        }

        $lastFiles = $currentFiles.FullName
    }

    Start-Sleep -Seconds 5
}
