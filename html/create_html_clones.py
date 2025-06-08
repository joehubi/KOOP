import shutil
import os

# Das Skript wird im html-Ordner ausgeführt
script_dir = os.path.dirname(os.path.abspath(__file__))
source_file = os.path.join(script_dir, "Koop_n.html")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, "mylist", "templates")

for n in range(1, 16):
    dest_file = os.path.join(template_dir, f"Koop_{n}.html")
    shutil.copyfile(source_file, dest_file)
    print(f"Kopiert: Koop_n.html -> Koop_{n}.html")