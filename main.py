from datetime import datetime, timedelta
import pyfiglet
import time
import os

def art():
    print(pyfiglet.figlet_format("X_Restore"))

def backup():
    current_date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = f"backup_{current_date_and_time}"
    
    # Create backup directory
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Backup folder '{backup_folder}' created.")
    
    # Perform backup (this is a placeholder, actual backup code should be implemented here)
    # For demonstration, creating a dummy file in the backup folder
    with open(f"{backup_folder}/backup.txt", "w") as f:
        f.write("This is a dummy backup file.")
    
    print(f"Backup completed in '{backup_folder}'.")

def schedule_backup(hour, minute):
    while True:
        now = datetime.now()
        if now.hour == hour and now.minute == minute:
            backup()
            break
        time.sleep(60)  # Sleep for 60 seconds and check again



def full_backup(PATH):
    try:
    #full system backup

        if os.path.isdir(PATH):
            # Take action if DIR exists.
            print(f"Perform backup  {PATH}...")
            os.system("sudo tar -cvpzf "+PATH+" --exclude=/proc --exclude=/tmp --exclude=/dev --exclude=/sys --exclude=/lost+found --exclude=/mnt --exclude=/media /")
        else :
            raise ValueError("Invalid PATH: {PATH}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid PATH.")
    


    
def specific_backup(SRC, PATH):
    #secific Directory backup
    
    print()

    try:
    #full system backup

        if os.path.isdir(PATH):
            # Take action if DIR exists.
            print(f"Perform backup  {PATH}...")
            os.system("sudo tar -cvpzf"+ PATH + SRC)
        else :
            raise ValueError("Invalid PATH: {PATH}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid PATH.")
    

if __name__ == "__main__":
    art()
    
    # Get backup time from user
    try:
        hour = int(input("Enter the hour to schedule backup (0-23): "))
        minute = int(input("Enter the minute to schedule backup (0-59): "))
        
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            raise ValueError("Invalid hour or minute.")
        
        print(f"Backup scheduled for {hour:02d}:{minute:02d}.")
        
        schedule_backup(hour, minute)
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid hour and minute.")