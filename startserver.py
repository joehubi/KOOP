import os
import subprocess

project_directory = os.getcwd()

# Aktiviere die virtuelle Python-Umgebung
activate_script = os.path.join(project_directory, 'venv', 'Scripts', 'activate')
activate_command = f'call "{activate_script}"'
subprocess.call(activate_command, shell=True)

# Führe den Django-Entwicklungsserver aus
runserver_command = f'python {os.path.join(project_directory, "manage.py")} runserver 0.0.0.0:8000'
subprocess.call(runserver_command, shell=True)
