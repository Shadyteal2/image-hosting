import os
import time
import subprocess
from PIL import Image

# Setup
INPUT_DIR = "input"
OUTPUT_DIR = "assets"
QUALITY = 80 

def run_git():
    print("Syncing with GitHub...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Vibecode Upload"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    if not os.path.exists(INPUT_DIR): os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg', 'webp'))]

    if not files:
        print("Nothing to process in /input.")
        return

    for filename in files:
        # Create unique name: ss_20260311_1230.webp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        new_name = f"ss_{timestamp}.webp"
        
        with Image.open(os.path.join(INPUT_DIR, filename)) as img:
            img.save(os.path.join(OUTPUT_DIR, new_name), "webp", quality=QUALITY)
            print(f"Processed: {new_name}")
        
        os.remove(os.path.join(INPUT_DIR, filename))
        time.sleep(1.1) # Prevents filename collision

    run_git()
    print("\nDone! Images are live.")

if __name__ == "__main__":
    main()