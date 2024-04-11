import os
import urllib.request
import ssl
import subprocess

def download_pip(url):
    try:
        # Create a directory to store the get-pip.py script
        os.makedirs('temp', exist_ok=True)
        
        # Download get-pip.py
        urllib.request.urlretrieve(url, 'temp/get-pip.py')
        
        print("get-pip.py downloaded successfully.")
        
        return True
    except Exception as e:
        print(f"Error downloading get-pip.py: {e}")
        return False

def install_pip():
    try:
        # Run get-pip.py to install pip
        result = subprocess.run(['python', 'temp/get-pip.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("pip installed successfully.")
            return True
        else:
            print(f"Error installing pip: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error installing pip: {e}")
        return False

if __name__ == "__main__":
    # Disable SSL certificate verification (not recommended for production)
    ssl._create_default_https_context = ssl._create_unverified_context

    # URL to download get-pip.py
    url = 'https://bootstrap.pypa.io/get-pip.py'
    
    if download_pip(url):
        install_pip()

    # Clean up
    os.remove('temp/get-pip.py')
    os.rmdir('temp')
