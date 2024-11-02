import time
from getpass import getuser
import os
import sys
import requests
import subprocess


program_path = os.path.dirname(os.path.realpath(__file__))
mmc_appdata = "C:\\Users\\" + getuser() + "\\AppData\\Local\\MCULauncher"
dotminecraft_folder_install = mmc_appdata + "\\minecraft\\install"
dotminecraft_folder_instances = mmc_appdata + "\\minecraft\\instances"
mcupackage_temp_install_path = "C:\\Users\\" + getuser() + "\\AppData\\Local\\MCULauncher\\TEMP"
mmc_is_installed_file = "C:\\Users\\" + getuser() + "\\AppData\\Local\\MCULauncher\\mmc_is_installed.txt"
current_version_file = "C:\\Users\\" + getuser() + "\\AppData\\Local\\MCULauncher\\current_version.txt"
latest_version_url = 'https://raw.githubusercontent.com/ConStrum/mcupackage2/refs/heads/main/version.txt'
update_file_url = 'https://raw.githubusercontent.com/ConStrum/mcupackage2/refs/heads/main/update.py'
update_downloaded_file = "C:\\Users\\" + getuser() + "\\AppData\\Local\\MCULauncher\\latest_update.py"
minecraft_launcher_file = dotminecraft_folder_install + "\\minecraft.exe"




reliquary_download = 'https://www.curseforge.com/api/v1/mods/241319/files/5860336/download'

response = requests.get(reliquary_download)

new_mod_file = dotminecraft_folder_instances + "\\mods\\reliquary-1.21.1-2.0.44.1245.jar"

with open(new_mod_file, 'wb') as f:
    f.write(response.content)
    f.close()

with open(current_version_file, 'w') as f:
    f.write("0.6")
    f.close()


run_minecraft_launcher_file_args = minecraft_launcher_file, "--workdir", dotminecraft_folder_install
subprocess.Popen(run_minecraft_launcher_file_args)
sys.exit(0)