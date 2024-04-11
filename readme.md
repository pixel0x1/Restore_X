
Certainly! Below is a README.md file for your backup application:

X_Restore Backup Application
Overview
X_Restore is a Python-based backup application that allows you to perform system backups or specific directory backups on a Linux system. It provides a simple UI using tkinter for scheduling backups at chosen times.

Features
Full System Backup: Backs up the entire Linux system excluding certain directories.
Specific Directory Backup: Backs up a specific directory.
Backup Scheduler: Allows scheduling of backups at chosen times using a simple UI.
Immediate Backup: Provides an option to perform a backup immediately.
Requirements
Python 3.x

pyfiglet library (for the ASCII art title)
Installation
Clone the repository:



git clone https://github.com/your_username/X_Restore.git


Install the required Python packages:
Copy code
pip install pyfiglet

Usage
Running the Application
Run the main_ui.py script to launch the backup application:

bash
Copy code
python backup_ui.py
Backup Options
Full System Backup:

Select the "Backup Now" button to perform a full system backup immediately.
Specific Directory Backup:

In the "Specific Directory Backup" section, enter the source directory and the backup path.
Click the "Backup Now" button to perform a backup of the specific directory immediately.
Scheduling a Backup
Enter the hour and minute to schedule the backup in the "Backup Scheduler" section.
Click the "Schedule Backup" button to schedule the backup.
Example

python main.py
Enter the hour and minute to schedule the backup when prompted. The application will run in the background and perform the backup at the specified time.

License
This project is licensed under the MIT License. See the LICENSE file for details.