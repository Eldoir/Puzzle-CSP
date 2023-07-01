import os
import subprocess

ui_folder = "app/ui/"

for file in os.listdir(ui_folder):
    if file.endswith(".ui"):
        file_path = os.path.join(ui_folder, file)
        output_file = os.path.splitext(file_path)[0] + ".py"
        subprocess.run(["pyuic5", file_path, "-o", output_file])

print("UI files converted to Python successfully.")