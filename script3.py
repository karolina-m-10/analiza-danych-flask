import subprocess

# Tworzenie wirtualnego środowiska
subprocess.run(['python3', '-m', 'venv', 'venv'])

# Informacja do użytkownika
print("Po aktywacji środowiska uruchom: pip install -r requirements.txt")
