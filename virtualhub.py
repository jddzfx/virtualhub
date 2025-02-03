import os
import subprocess
import ctypes
import time

class VirtualHub:
    def __init__(self):
        self.os_type = os.name

    def apply_updates(self):
        """Applies critical updates on Windows-operated devices."""
        if self.os_type == 'nt':
            print("Applying critical updates...")
            try:
                subprocess.run(['powershell', '-Command', 'Install-WindowsUpdate', '-AcceptAll', '-AutoReboot'], check=True)
                print("Updates applied successfully.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while applying updates: {e}")
        else:
            print("This function is only supported on Windows systems.")

    def tweak_power_management(self):
        """Applies power management tweaks to enhance device longevity."""
        if self.os_type == 'nt':
            print("Tweaking power management settings...")
            try:
                # Set power plan to 'Power Saver'
                subprocess.run(['powercfg', '/SETACTIVE', 'a1841308-3541-4fab-bc81-f71556f20b4a'], check=True)
                # Disable fast startup
                subprocess.run(['powercfg', '/hibernate', 'off'], check=True)
                print("Power management settings adjusted successfully.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while tweaking power management: {e}")
        else:
            print("This function is only supported on Windows systems.")

    def run(self):
        """Executes the update and power management tasks."""
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("This program requires administrator privileges. Please run as administrator.")
            return
        
        self.apply_updates()
        time.sleep(5)  # Wait for a few seconds before proceeding
        self.tweak_power_management()

if __name__ == "__main__":
    virtual_hub = VirtualHub()
    virtual_hub.run()