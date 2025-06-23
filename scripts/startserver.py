import os
import subprocess


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Aktiviere die virtuelle Python-Umgebung
activate_script = os.path.join(base_dir, 'venv', 'Scripts', 'activate')
activate_command = f'call "{activate_script}"'
subprocess.call(activate_command, shell=True)

# Führe den Django-Entwicklungsserver aus
runserver_command = f'python {os.path.join(base_dir, "manage.py")} runserver 0.0.0.0:8000'
subprocess.call(runserver_command, shell=True)
