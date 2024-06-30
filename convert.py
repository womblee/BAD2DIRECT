import argparse
import re
import pyperclip
import time

def validate_url(url):
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    
    pattern = r'https://drive\.google\.com/file/d/([a-zA-Z0-9_-]+)(?:/view)?(?:\?usp=(?:sharing|drive_link))?$'
    match = re.match(pattern, url)
    
    if not match:
        raise ValueError("Invalid Google Drive URL format.")
    
    return match.group(1)

def create_direct_link(file_id):
    return f"https://drive.google.com/uc?id={file_id}&export=download&confirm=t"

def main():
    parser = argparse.ArgumentParser(
        description='BAD2DIRECT - Converts Google Drive sharing links to direct download links'
    )
    parser.add_argument('--link', type=str, required=True, help='Google Drive sharing link')
    
    args = parser.parse_args()
    
    try:
        file_id = validate_url(args.link)
        direct_link = create_direct_link(file_id)
        print("\n" + direct_link)
        
        # Copy to clipboard
        pyperclip.copy(direct_link)
        
        # Wait for a moment to ensure clipboard operation is complete
        time.sleep(0.5)
        
        # Print status after two new lines
        print("\nDirect link copied to clipboard!")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except pyperclip.PyperclipException:
        print("\n\nWarning: Unable to copy to clipboard. Make sure you have the required dependencies installed.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
