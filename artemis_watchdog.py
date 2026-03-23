import os
import time
from datetime import datetime

LOG_FILE = "access_logs.txt"

def monitor_access():
    print("--- ARTEMIS WATCHDOG: ACTIVE ---")
    print(f"Monitoring access to 'artemis_broadcast_node.json'...")
    
    # Get initial 'last modified' time
    last_mod = os.path.getmtime("artemis_broadcast_node.json")
    
    try:
        while True:
            current_mod = os.path.getmtime("artemis_broadcast_node.json")
            if current_mod != last_mod:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(LOG_FILE, "a") as f:
                    f.write(f"[{timestamp}] NODE ACCESSED / PINGED BY RESEARCHER\n")
                print(f"ALERT: Node accessed at {timestamp}")
                last_mod = current_mod
            time.sleep(10) # Checks every 10 seconds
    except KeyboardInterrupt:
        print("\nWATCHDOG STANDBY.")

if __name__ == "__main__":
    monitor_access()
